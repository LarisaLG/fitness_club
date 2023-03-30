from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('trainer_profile/', views.trainer_profile, name='trainer_profile'),
    path('update_trainer_profile/', views.update_trainer_profile, name='update_trainer_profile'),
]
