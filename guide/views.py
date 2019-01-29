from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RegistrationForm, ServiceForm
from django.contrib import messages
from .models import UserServices
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView

from django.forms.models import inlineformset_factory
def home(request):
     return render(request , 'guide/index.html')

def register(request):

     if request.method=='POST':
          form = RegistrationForm(request.POST)
          if form.is_valid():
               form.save()
               username = form.cleaned_data.get('username')
               messages.success(request, f'Your account has created you can now log in!')
               return redirect('login')

     else:
          form=RegistrationForm()
     return render(request, 'guide/register.html', {'form':form})

@login_required
def dashboard(request):
     context = {
          'posts': UserServices.objects.all
     }
     return render(request , 'guide/dashboard.html' , context)

@login_required
def setService(request):
     u = UserServices.objects.get(user=request.user)
     if request.method=='POST':
          # data = request.POST.copy()
          # data.update({'user': request.user.pk })
          s_form = ServiceForm( request.POST , request.FILES , instance = u)
          if s_form.is_valid():
               # s_form.user = request.user
               s_form.save()
               # x.user = request.user
               # x.save()
               return redirect('dashboard')
     else:
          s_form = ServiceForm(instance = u)
     return render(request , 'guide/service.html', {'s_form':s_form})

@login_required
def Profile(request):
     return render(request , 'guide/profile.html')