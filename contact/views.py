from django.shortcuts import render
from .forms import ContactUsForm


def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContactUsForm()
    return render(request, 'contact/contacts.html', {'form': form})
