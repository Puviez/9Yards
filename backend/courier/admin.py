from django.contrib import admin
from .models import CustomUser, Package, Courier

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser

class PackageAdmin(admin.ModelAdmin):
    model = Package
    list_display = ('description', 'status', 'sender', 'receiver')

class CourierAdmin(admin.ModelAdmin):
    model = Courier
    list_display = ('name', 'status', 'package')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Package, PackageAdmin)
admin.site.register(Courier, CourierAdmin)