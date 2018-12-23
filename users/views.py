from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
	return HttpResponse("hello world")

def register(request):
	form = UserCreationForm(request.POST or None)
	if form.is_valid():
		form.save()
	return render(request, 'users/register.html', {'form' : form})

