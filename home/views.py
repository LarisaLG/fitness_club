from django.shortcuts import render

# Create your views here.


def index(request):
    """A view to return index page """
    return render(request, 'home/index.html')


def about(request):
    """
    This view renders to the user the About page.
    """
    return render(request, 'home/about.html')
