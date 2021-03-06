from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
  email = forms.EmailField()

  class Meta:
      model = User
      fields = ['username', 'email']

class CommonForm(forms.ModelForm):
    def sbadmin_format(self, model, data):
        for i in range(len(data)):
            for j in range(len(data[i])):
                field = self.fields[data[i][j][0]]
                if len(data[i][j]) == 3:
                    data[i][j].append(data[i][j][0].replace("_", " ").title())
                if field.required:
                    data[i][j][-1] = data[i][j][-1] + "*"
                data[i][j].insert(0, field.get_bound_field(self, data[i][j][0]))
                data[i][j].append(field)
        return data

class AccessoryForm(CommonForm):
    class Meta:
        model = Accessory
        exclude = ["user", "id", "slug"]

    def sbadmin_format(self):
        data = [
            [["name", 4, "text"], ["status", 4, "select"], ["cost", 4, "number"]],
            [["sell_price", 4, "number"], ["aftermarket_seller", 4, "text"], ["manufacturer", 4, "text"]],
            [["notes", 12, "text"]],
        ]
        return super().sbadmin_format(Accessory, data)

class ArtisanForm(CommonForm):
    class Meta:
        model = Artisan
        exclude = ["user", "id", "slug"]
    
    def sbadmin_format(self):
        data = [
            [["name", 4, "text"], ["status", 4, "select"], ["cost", 4, "number"]],
            [["sell_price", 4, "number"], ["build", 4, "select"], ["profile", 4, "text"]],
            [["aftermarket_seller", 4, "text"], ["manufacturer", 4, "text"], ["documentation", 4, "text"]],
            [["notes", 12, "text"]],
        ]
        return super().sbadmin_format(Artisan, data)

class BuildForm(CommonForm):
    class Meta:
        model = Build
        exclude = ["user", "id", "slug"]

    def sbadmin_format(self):
        data = [
            [["name", 12, "text"],],
            [["keyboard", 4, "select"], ["keycap", 4, "select"], ["switch", 4, "select"]],
            [["notes", 12, "text"]],
        ]
        return super().sbadmin_format(Build, data)

class KeyboardForm(CommonForm):
    class Meta:
        model = Keyboard
        exclude = ["user", "id", "slug"]

    def sbadmin_format(self):
        data = [
            [["name", 4, "text"], ["status", 4, "select"], ["cost", 4, "number"]],
            [["sell_price", 4, "number"], ["aftermarket_seller", 4, "text"], ["manufacturer", 4, "text"]],
            [["size", 4, "select"], ["layout", 4, "text"], ["color", 4, "text"]],
            [["pcb", 6, "text", "Current PCB"], ["plate", 6, "text"]],
            [["mount", 6, "text"], ["foam", 6, "text"]],
            [["stabilizers", 6, "text"], ["stabilizer_cost", 6, "number"]],
            [["material", 6, "text"], ["weight", 6, "text", "Base/Weight"]],
            [["accessories", 12, "text"]],
            [["front_height", 4, "number"], ["typing_angle", 4, "number"], ["carrying_case", 4, "text"]],
            [["extra_pcbs", 6, "text", "Extra PCBs"], ["extra_plates", 6, "text"]],
            [["extra_accessories", 12, "text"]],
            [["notes", 12, "text"]],
        ]
        return super().sbadmin_format(Keyboard, data)

class KeycapForm(CommonForm):
    class Meta:
        model = Keycap
        exclude = ["user", "id", "slug"]

    def sbadmin_format(self):
        data = [
            [["name", 4, "text"], ["status", 4, "select"], ["cost", 4, "number"]],
            [["sell_price", 4, "number"], ["aftermarket_seller", 4, "text"], ["profile", 4, "text"]],            
            [["production", 6, "select"], ["material", 6, "text"]],
            [["sets", 6, "text"], ["manufacturer", 6, "text"]],
            [["notes", 12, "text"]],
        ]
        return super().sbadmin_format(Keycap, data)

class SwitchForm(CommonForm):
    class Meta:
        model = Switch
        exclude = ["user", "id", "slug"]

    def sbadmin_format(self):
        data = [
            [["name", 4, "text"], ["status", 4, "select"], ["cost", 4, "number"]],
            [["sell_price", 4, "number"], ["number", 4, "number"], ["switch_type", 4, "select"]],            
            [["actuation_force", 4, "number", "Actuation Force (g)"], ["bottom_out_force", 4, "number", "Bottom-Out Force (g)"], ["spring_length", 4, "text"]],
            [["lube", 6, "text"], ["film", 6, "text"]],
            [["aftermarket_seller", 6, "text"], ["manufacturer", 6, "text"]],
            [["top_material", 6, "text"], ["bottom_material", 6, "text"]],
            [["stem_material", 6, "text"], ["spring_material", 6, "text"]],
            [["notes", 12, "text"]],
        ]
        return super().sbadmin_format(Switch, data)
