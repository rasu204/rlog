from django.shortcuts import render
from .forms import AgencyForm
from rlogsystem.models import CandidateStatus

def index22(request):

	form = AgencyForm()

	if request.method =='POST':
		form = AgencyForm(request.POST)
		if form.is_valid():
			form.save()
	context = { 'form':form}
	return render(request,'agencyform.html',context)

def index23(request):
	results=CandidateStatus.objects.all()
	return render (request,'candtable.html',{"data":results})