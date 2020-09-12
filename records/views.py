from django.shortcuts import render
from django.http import HttpResponse
from .models import Staging, GoodRecords, BadRecords
from django_pandas.io import read_frame

def index2(request):
    df = read_frame(Staging.objects.all())
    good = read_frame(GoodRecords.objects.all())
    bad = read_frame(BadRecords.objects.all())
    df = df.astype(str)
    # df['total_exp'] = df['total_exp'].astype(str)

    # x = df['total_exp'].str.isdecimal()
    # if ~x:
    #     df['reason'] = 'Not Int/Float'
    dict = {'contact_details_phone2':'Same as Phone 1'}
    # if (~df['total_exp'].str.isdecimal()):
    df.loc[df['contact_details_mobile'].str.len() != 10, 'reason'] = 'Not 10 digits'

    df.loc[df['contact_details_phone2'].str.len() != 10, 'reason'] = 'Not 10 digits'
    df.loc[df['contact_details_phone2'] == df['contact_details_mobile'], 'reason'] = [dict]

    bad = df.loc[df['reason'] != 'None']
    good = df.loc[df['reason'] == '']
    return HttpResponse(bad.to_html())
