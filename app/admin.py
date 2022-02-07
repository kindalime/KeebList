from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in User._meta.get_fields()]

@admin.register(Accessory)
class AccessoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Accessory._meta.get_fields()]

@admin.register(Artisan)
class ArtisanAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Artisan._meta.get_fields()]

@admin.register(Build)
class BuildAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Build._meta.get_fields()]

@admin.register(Keyboard)
class KeyboardAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Keyboard._meta.get_fields()]

@admin.register(Keycap)
class KeycapAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Keycap._meta.get_fields()]

@admin.register(Switch)
class SwitchAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Switch._meta.get_fields()]
