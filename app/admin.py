from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Accessory)
class AccessoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Artisan)
class ArtisanAdmin(admin.ModelAdmin):
    pass

@admin.register(Build)
class BuildAdmin(admin.ModelAdmin):
    pass

@admin.register(Keyboard)
class KeyboardAdmin(admin.ModelAdmin):
    pass

@admin.register(Keycap)
class KeycapAdmin(admin.ModelAdmin):
    pass

@admin.register(Switch)
class SwitchAdmin(admin.ModelAdmin):
    pass
