from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import UserCreateForm

def home(request):
	return render(request,'accounts/login')


class SignUp(CreateView):
    form_class = UserCreateForm
    success_url = '/login/'
    template_name = 'accounts/signup.html'
