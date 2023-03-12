from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Profile
from allauth.account.forms import SignupForm


# User form
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('mob_phone', 'avatar')
