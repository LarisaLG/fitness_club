from django.shortcuts import render, redirect
from contact.forms import ContactUsForm
from django.core.mail import send_mail
from django.contrib import messages


# Create your views here.


def index(request):
    """A view to return index page """
    return render(request, 'home/index.html')


def about(request):
    """
    This view renders to the user the About page.
    """
    return render(request, 'home/about.html')


# Send e-mail for call back
# Code from CI lesson: Sending Real Emails with Django and
# Code With Stein tutorial https://www.youtube.com/watch?v=dnhEnF7_RyM
def callback(request):
    if request.method == 'POST':
        form = contat.form.ContactUsForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            form.save()
            send_mail(name, message, from_email, ['info@ponigym.com'])
            messages.success(request,
                             f'Your message successfully send.')
            return redirect('index')
    else:
        form = ContactUsForm()
    return render(request, 'home/index.html', {'form': form})
