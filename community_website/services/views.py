from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Service, User
from .forms import ServiceForm

# Create your views here.

def home(request):
	service_list = Service.objects.all()

	return render(request, 'services/home.html', {'service_list':service_list})


def add_service(request):
	submitted = False

	if request.method == "POST":
		form = ServiceForm(request.POST, request.FILES)

		if form.is_valid():

			#service = form.save(commit=False)
			#service.provider = request.user.id # Logged in user First Name
			#service.save()
			
			form.save()
			return HttpResponseRedirect('/add_service?submitted=True')

	else:
		form = ServiceForm
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'services/add_service.html', {'form':form, 'submitted':submitted})


def search_providers(request):
	if request.method == "POST":
		searched = request.POST['searched']

		providers = User.objects.filter(first_name__contains=searched) or User.objects.filter(last_name__contains=searched)

		return render(request, 'services/search_providers.html', {'searched':searched, 'providers':providers})

	else: 
		return render(request, 'services/search_providers.html', {})


def provider_profile(request, user_id):
	provider_id = Service.objects.filter(provider_id=user_id)
	#user_id = User.objects.filter(user_id=provider)


	return render(request, 'services/provider_profile.html', {'provider_id':provider_id})
