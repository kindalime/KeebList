from django import forms
from .models import *

class CommonForm(forms.ModelForm):
    pass

class ArticleForm(CommonForm):
    class Meta:
        model = Article
        fields = "__all__"

class AccessoryForm(CommonForm):
    class Meta:
        model = Accessory
        fields = "__all__"

class BuildForm(forms.ModelForm):
    class Meta:
        model = Build
        fields = "__all__"

class KeyboardForm(CommonForm):
    class Meta:
        model = Keyboard
        fields = "__all__"

class KeycapForm(KeycapForm):
    class Meta:
        model = Keycap
        fields = "__all__"

class SwitchForm(SwitchForm):
    class Meta:
        model = Switch
        fields = "__all__"
