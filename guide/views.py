from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RegistrationForm
from django.contrib import messages
# from .models import UserProfile 
from django.contrib.auth.models import User

from django.forms.models import inlineformset_factory
def home(request):
     return render(request , 'guide/index.html')

def register(request):
     
     if request.method=='POST':
          form = RegistrationForm(request.POST)
          if form.is_valid():
               form.save()
               username = form.cleaned_data.get('username')
               messages.success(request, f'Account created for {username}!')
               return redirect('home')

     else:
          form=RegistrationForm()          
     return render(request, 'guide/register.html', {'form':form})
# Create your views here.
