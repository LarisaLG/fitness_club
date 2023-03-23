from django import forms
from .models import ContactUs


# Create contact form
class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control border',
                       'placeholder': 'Your name'}),
            'email': forms.EmailInput(
                attrs={'class': 'form-control border',
                       'placeholder': 'Your email'}),
            'subject': forms.TextInput(
                attrs={'class': 'form-control border',
                       'placeholder': 'Subject'}),
            'message': forms.Textarea(
                attrs={'class': 'form-control border',
                       'placeholder': 'Your message'}),
        }
        labels = {
            'name': '',
            'email': '',
            'subject': '',
            'message': '',
        }
