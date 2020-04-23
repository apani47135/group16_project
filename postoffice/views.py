from django.shortcuts import render, redirect
from .models import branches
from .models import Packages
from .models import package_history
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .trackform import trackingForm
from django.contrib import messages
from .forms import ExampleForm
from django.views.decorators.csrf import ensure_csrf_cookie


def home(request):
	if request.method =="POST":
		form = trackingForm(request.POST)
		item =None
		if form.is_valid():
			id = form.cleaned_data.get('tracking_id')

			try:
				item = Packages.objects.get(package_ID=id)
			except Packages.DoesNotExist:
				messages.warning(request,f'Tracking number does not exist ')
				return redirect('po-home')
			
			
	
			context = {
			'item':item,
			'my_package' : item.locations.all().order_by('-creation_date'),
			'branch': branches.objects.all(),
			}
			return render(request, 'postoffice/result.html',context)
	else:
		form = request.POST

	return render(request, 'postoffice/home.html',{'form':form})

def about(request):
	context = {
		'branch': branches.objects.all(),
		
	}
	return render(request, 'postoffice/about.html',context)

def reports(request):
	context ={}
	context['form'] = ExampleForm()
	if request.method=="POST":
		temp = request.POST
		start =temp['start_date']
		end =temp['end_date']
		q = Packages.objects.filter(order_date__range=[start,end])
		print(q)
		context={'pack': q}
		return render(request, 'postoffice/outgoing.html',context)

	return render(request, 'postoffice/reports.html',context)

def delivered(request):
	context ={}
	context['form'] = ExampleForm()
	if request.method=="POST":
		temp = request.POST
		start =temp['start_date']
		end =temp['end_date']
		q = Packages.objects.filter(order_date__range=[start,end],delivery_status=True)
		print(q)
		context={'pack': q}
		return render(request, 'postoffice/out-delivered.html',context)

	return render(request, 'postoffice/delivered.html',context)



def history(request):
	a = Packages.objects.get(package_ID="1234")
	
	context = {
		'my_package' : a.locations.all().order_by('-creation_date'),
		'branch': branches.objects.all(),
		}
	return render(request, 'postoffice/history.html',context)
	


def result(request):
	return render(request, 'postoffice/result.html')

# def track(request):
	
# 	if request.method =="POST":
# 		form = trackingForm(request.POST)
# 		if form.is_valid():
# 			id = form.cleaned_data.get('tracking_id')
# 			item = Packages.objects.get(package_ID=id)
# 			messages.success(request,f'SUCCESS {id}')

# 			return render(request, 'postoffice/result.html',{'item':item})
# 	else:
# 		form = trackingForm	()

	
# 	return render(request, "postoffice/track.html",{'form':form})

