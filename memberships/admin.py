from django.contrib import admin
from .models import Package, PackDetail

# Register your models here.


class PackageAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')

    class Meta:
        ordering = ["price"]


class PackDetailAdmin(admin.ModelAdmin):
    list_display = ('title', 'package')

    class Meta:
        ordering = ['title', 'package']


admin.site.register(Package, PackageAdmin)
admin.site.register(PackDetail, PackDetailAdmin)
