from django import forms
from .models import ContactUs


# Create contact form
class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'message']
