from django.contrib import admin
from .models import *

# Register your models here.


class TrainerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'specialization',
                    'mob_phone', 'email', 'date_of_birth', 'date_joined',
                    'is_staff', 'is_available')
    exclude = ('profile_avatar',)
    list_filter = ('first_name', 'last_name', 'specialization', 'date_joined')

    class Meta:
        ordering = ['get_full_name']


class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Trainer, TrainerAdmin)
admin.site.register(Specialization, SpecializationAdmin)
admin.site.register(Profile)
