from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Profile, Trainer, Specialization
from allauth.account.forms import SignupForm


# User form
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')


# User profile form
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('mob_phone', 'avatar')


# Trainer profile form
class TrainerProfileForm(ModelForm):
    class Meta:
        model = Trainer
        fields = ('first_name', 'last_name', 'email', 'mob_phone',
                  'profile_avatar', 'specialization',
                  'is_available')
        widgets = {
            'specialization':
            forms.Select(choices=Specialization.objects.all()),
            'is_available': forms.CheckboxInput()
        }
