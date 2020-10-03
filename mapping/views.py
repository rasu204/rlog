from django.shortcuts import render
from .models import Mapping
from records.models import Staging
from django.shortcuts import render, redirect
from records.forms import Staging_form
from django.http import HttpResponse
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import os
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.shortcuts import get_object_or_404
import json
import datetime
from pprint import pprint
from django.forms.models import model_to_dict

# Create your views here.
CSV_STORAGE = os.path.join(os.getcwd(), 'static', 'csv')


def choose(request):
    if request.method == 'POST':
        if request.POST.get('checkBox') == None:
            return redirect('/import')

        return redirect('/import_p')
    else:
        return render(request, 'Choose.html')


@csrf_exempt
def import_data(request):
    if request.method == 'POST':
        new_students = request.FILES['myfile']
        if new_students.content_type == 'text/csv':
            df = pd.read_csv(new_students)
        else:
            df = pd.read_excel(new_students)  # make sure that there' no header
        path_name = os.path.join('static', 'tempcsv', 'temp.csv')
        df.to_csv(path_name, index=False)
        return redirect('/fieldmatching?df=' + path_name)
    else:
        return render(request, 'import_data.html')


def fieldmatching(request):
    if request.method == 'POST':
        path_name = request.POST['path_name']
        df = pd.read_csv(path_name)
        names = list(df.columns)
        fields = [field.name for field in Staging._meta.get_fields()]
        df = df.transform(lambda x: x.fillna('None') if x.dtype == 'object' else x.fillna(0))
        if request.POST.get('checkBox') == None:
            matched = {key: request.POST.get(key, False) for key in fields}
            x = list(matched.keys())
            y = list(matched.values())
            dict = {}
            for key in y:
                for value in x:
                    dict[key] = value
                    print(dict)
                    x.remove(value)
                    break
            # print(dict)
            df.rename(columns=dict, inplace=True)
        # df.drop('id', axis=1, inplace=True)
        # df.set_index("id", drop=True, inplace=True)

        dictionary = df.to_dict(orient="index")
        # box = Mapping()
        # box.MappingFor = 'Staging'
        # box.UserID = '1'
        # box.Mappings = dict
        # a = {Mapping.objects.all()[0].Mappings}
        # a = Mapping.objects.all()[0].Mappings
        # print(a)
        Mapping.objects.create(MappingFor='Staging', Mappings=dict)
        print(Mapping.objects.all()[0].Mappings)
        save_dict(dictionary)
        # for index, object in dictionary.items():
        # m = Staging()
        # for k, v in object.items():
        # setattr(m, k, v)
        # setattr(m, 'id', index)
        # m.save()
        return render(request, 'import_data.html')
    else:
        path_name = request.GET.get('df')
        df = pd.read_csv(path_name)
        names = list(df.columns)
        fields = [field.name for field in Staging._meta.get_fields()]
        return render(request, 'fieldmatching.html',
                      {'fields': fields, 'path_name': path_name, 'names': names})


def disp(request):
    data = pd.read_excel(r"H:\Candidate Report.xlsx")
    df = []
    db = []
    context = {
        'df': list(data.columns),
        'db': list(field.name for field in Staging._meta.get_fields())
    }

    return render(request, 'mapping.html', context)


def save_dict(dictionary):
    for index, object in dictionary.items():
        m = Staging()
        for k, v in object.items():
            setattr(m, k, v)
        setattr(m, 'id', index)
        m.save()


def import_data_p(request):
    if request.method == 'POST':
        new_students = request.FILES['myfile']
        if new_students.content_type == 'text/csv':
            df = pd.read_csv(new_students)
        else:
            df = pd.read_excel(new_students)  # make sure that there' no header
        path_name = os.path.join('static', 'tempcsv', 'temp.csv')
        df.to_csv(path_name, index=False)
        df = pd.read_csv(path_name)
        df = df.transform(lambda x: x.fillna('None') if x.dtype == 'object' else x.fillna(0))
        # declare store dictionary i.e we want dict
        print(Mapping.objects.all()[0].Mappings)
        p = Mapping.objects.all()[0].Mappings
        print(p)
        dict = {}
        print(dict)
        if not bool(p):
            print("No Previous Matching Columns Found")
            return redirect('/choose')
        else:
            df.rename(columns=p, inplace=True)
            dictionary = df.to_dict(orient="index")
            save_dict(dictionary)
            print("columns found")
        # save_dict(dictionary)
        return render(request, 'import_data.html')
    else:
        return render(request, 'import_data.html')
