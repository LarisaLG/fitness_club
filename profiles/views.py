from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile, Trainer
from .forms import UserForm, ProfileForm, TrainerProfileForm
from django.contrib import messages


# User profile page
@login_required
def profile(request):
    return render(request, 'profiles/profile.html')


# Update user profile page
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


# Trainer profile page
@login_required
def trainer_profile(request):
    user = request.user
    try:
        trainer = Trainer.objects.get(user=user)
    except Trainer.DoesNotExist:
        trainer = None

    return render(request, 'profiles/trainer_profile.html',
                  {'trainer': trainer})


# Update Trainer Profile page
@login_required
def update_trainer_profile(request):
    if request.user.is_authenticated:
        user = request.user
        """ Check if user has a Trainer object
        and creates profile  """
        try:
            trainer = user.trainer
        except Trainer.DoesNotExist:
            trainer = Trainer.objects.create(user=user)
        if request.method == 'POST':
            trainer = user.trainer
            if request.method == 'POST':
                user_form = UserForm(request.POST, instance=user)
                trainer_form = TrainerProfileForm(request.POST, request.FILES,
                                           instance=trainer)
                if user_form.is_valid() and trainer_form.is_valid():
                    user_form.save()
                    trainer_form.save()
                    messages.success(request,
                                     f'Your profile successfully updated.')
                    return redirect('trainer_profile')
        else:
            user_form = UserForm(instance=user)
            trainer_form = TrainerProfileForm(instance=trainer)

        context = {
            'user_form': user_form,
            'trainer_form': trainer_form,
            'user': user,
            'trainer': trainer,
        }
    return render(request, 'profiles/update_trainer_profile.html', context)