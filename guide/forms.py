from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserServices , Review


class RegistrationForm (UserCreationForm):
    # email=forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email', 'password1', 'password2']

class ServiceForm(forms.ModelForm):
    
    class Meta:
        model = UserServices

        fields = ['name_of_service', 'location','short_description', 'type_of_service', 'details','image','special_features' ,'user']
        widgets = {
            'user': forms.HiddenInput,
        }

class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ['review']
        widgets = {
            'posts': forms.HiddenInput,
            'author': forms.HiddenInput,
            'date': forms.HiddenInput,
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['review'].widget.attrs['cols'] = 4
        self.fields['review'].widget.attrs['rows'] = 5
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

class BookForm(forms.Form):
    date = forms.DateField( required=True,widget=forms.DateInput(attrs={'placeholder': 'Enter date in dd/mm/yyy format'}))


 
        