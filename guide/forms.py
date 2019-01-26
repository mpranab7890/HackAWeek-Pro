from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class RegistrationForm (UserCreationForm):
    # email=forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email', 'password1', 'password2']


    
# def save(self, commit=True):
#     instance = super(RegistrationForm, self).save(commit=False)
#     instance.user = self.user
#     if commit:
#         instance.save()
#         return instance
    
# def save(self, commit=True):
#     user = super(UserCreationForm, self).save()
#     u = UserProfileInfo(user=user)
#     u.save()

     