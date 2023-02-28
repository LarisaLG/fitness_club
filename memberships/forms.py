from django import forms
# from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
# from django.contrib.auth.models import UserCreationForm
from allauth.account.forms import SignupForm


# Add custom fields to the allauth signup form
class CustomSignupForm(SignupForm):

    first_name = forms.CharField(max_length=50, label='First Name')
    last_name = forms.CharField(max_length=50, label='Last Name')

    class Meta:
        model = User
        fields = ('first_name', 'lastst_name', 'username', 'email', 'password1', 'password2')

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        return user
