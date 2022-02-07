from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class BaseCommonModel(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True
        ordering = ['-name']

    def get_absolute_url(self, model):
        return reverse(f'{model}-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.name

class CommonModel(BaseCommonModel):
    class Meta:
        abstract = True

class Keyboard(model.CommonModel):
    def get_absolute_url(self):
        return super().get_absolute_url("keyboard")

class Keycap(model.CommonModel):
    def get_absolute_url(self):
        return super().get_absolute_url("keycap")

class Switch(model.CommonModel):
    def get_absolute_url(self):
        return super().get_absolute_url("switch")

class Build(BaseCommonModel):
    name = models.CharField(max_length=255)
    keyboard = models.ForeignKey(Keyboard, on_delete=models.CASCADE)
    keycap = models.ForeignKey(Keycap, on_delete=models.CASCADE)
    switch = models.ForeignKey(Switch, on_delete=models.CASCADE)
    
    @property
    def present(self):
        pass
        # return keyboard.present and keycap.present and switch.present

    @property
    def cost(self):
        pass
        # return 

    def get_absolute_url(self):
        return super().get_absolute_url("build")

class Artisan(model.CommonModel):
    build = models.ForeignKey(Build, on_delete=models.SET_NULL)

    def get_absolute_url(self):
        return super().get_absolute_url("artisan")

class Accessory(model.CommonModel):
    def get_absolute_url(self):
        return super().get_absolute_url("accessory")
