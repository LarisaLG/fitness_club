from django.shortcuts import render


# Schedule page
def schedule(request):
    """
    This view renders to the user the Schedule page.
    """
    return render(request, 'trainers/schedule.html')
