from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import Account

class RegistrationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ['first_name','last_name','username','email','phone_number','password1','password2']

    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First-Name'})
    )
    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last-Name'})
    )
    username = forms.CharField(
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'})
    )
    email = forms.EmailField(
        required=True,
        max_length=100,
        widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'})
    )
    phone_number = forms.CharField(
        required=True,
        max_length=10,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Phone-Number'})
    )
    password1 = forms.CharField(
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your Password','type':'password'})
    )
    password2 = forms.CharField(
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'confirm Password','type':'password'})
    )
    

# sign in form & import authenticationform
class UserLoginForm(AuthenticationForm):
    email = forms.EmailField(
        required=True,
        max_length=100,
        widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email Address'})
    )

    password = forms.CharField(
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your Password','type':'password'})
    )    