from django import forms
from .models import Events
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#create event form
class Create_Event_Form(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['name', 'date', 'start_time', 'end_time', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'type': 'text','class': 'form-control name'}),
            'date': forms.DateInput(attrs={'type': 'date', 'min':datetime.date.today, 'class': 'form-control date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time','class': 'form-control start_time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time','class': 'form-control end_time'}),
            'description': forms.Textarea(attrs={'type': 'textarea','class': 'form-control description', 'rows':'5'}),
        }

# user registeration form
class RegisterUserForm(UserCreationForm):
      username = forms.CharField(max_length=256,label='Enter Username', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
      first_name = forms.CharField(max_length=256,label='Enter First Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
      last_name = forms.CharField(max_length=256,label='Enter Last Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
      email = forms.EmailField(max_length=256,label='Enter Email',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
      password1 = forms.CharField(max_length=256,label='Enter Password',widget=forms.PasswordInput(attrs={'type':'password','class': 'form-control', 'placeholder': 'Password'}))
      password2 = forms.CharField(max_length=256,label='Confirm Password',widget=forms.PasswordInput(attrs={'type':'password','class': 'form-control', 'placeholder': 'Confirm Password'}))
      
      class Meta:
            model = User
            fields = ("username","first_name","last_name", "email", "password1", "password2")

# user login form
class Login_form(forms.Form):
      username = forms.CharField(max_length=256,label='Enter Username', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
      password = forms.CharField(max_length=256,label='Enter Password',widget=forms.TextInput(attrs={'type': 'password','class': 'form-control', 'placeholder': 'Password'}))

#edit profile form 
class Profile_form(forms.ModelForm):
    username = forms.CharField(max_length=256,label='Enter Username', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    first_name = forms.CharField(max_length=256,required=False,label='Enter First Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=256,required=False,label='Enter Last Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    email = forms.EmailField(max_length=256,label='Enter Email',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
      
    class Meta:
          model = User
          fields = ['username', 'first_name','last_name', 'email']