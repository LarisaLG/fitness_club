from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from .forms import UserForm, ProfileForm
from django.contrib import messages


# Profile page
def profile(request):
    return render(request, 'profiles/profile.html')


# Update Profile page
@login_required
def update_profile(request):
    if request.user.is_authenticated:
        user = request.user
        """ Check if user has a Profile object
        and creates profile  """
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
                    messages.success(request,
                                     f'Your profile successfully updated.')
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
    return render(request, 'profiles/update_profile.html', context)


# Delete User Account
@login_required
def delete_account(request):
    """Existing and authenticated user can delete their account"""

    if request.user.is_authenticated:
        profile = Profile.objects.get(id=request.user.profile.id)
        user = request.user

        # Check that user really wants to delete this route
        if request.method == 'POST':
            user.delete()
            messages.success(request,
                             ('Your profile has been successfully deleted!'))
            return redirect('index')

        context = {
            'profile': profile,
        }

        return render(request, 'profiles/delete_account.html', context)
