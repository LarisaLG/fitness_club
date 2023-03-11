from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from .forms import UserForm, ProfileForm


# Profile page

@login_required
def profile(request):
    if request.user.is_authenticated:
        user = request.user
        """ Check if user has a Profile object """
        try:
            profile = user.profile
        except Profile.DoesNotExist:
            profile = Profile.objects.create(user=user)
        if request.method == 'POST':
            profile = user.profile
            if request.method == 'POST':
                user_form = UserForm(request.POST, instance=user)
                profile_form = ProfileForm(request.POST, request.FILES,
                                           instance=profile)
                if user_form.is_valid() and profile_form.is_valid():
                    user_form.save()
                    profile_form.save()
                    return redirect('profile')
        else:
            user_form = UserForm(instance=user)
            profile_form = ProfileForm(instance=profile)

        context = {
            'user_form': user_form,
            'profile_form': profile_form,
            'user': user,
            'profile': profile,
        }
    return render(request, 'profiles/profile.html', context)
