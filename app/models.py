from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField("email", blank=False)

class BaseCommonModel(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    notes=models.CharField(max_length=1024, blank=True)

    class Meta:
        abstract = True
        ordering = ['-name']

    def get_absolute_url(self, model):
        return reverse(f'{model}-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.name

class CommonModel(BaseCommonModel):
    status_choices=[
        ("Pre-GB", "Pre-GB"),
        ("Ordered GB", "Ordered GB"),
        ("Ordered In-Stock", "Ordered In-Stock"),
        ("Shipping", "Shipping"),
        ("Present", "Present"),
        ("Sold", "Sold"),
    ]

    status=models.CharField(max_length=255, choices=status_choices)
    cost=models.FloatField()
    aftermarket_seller=models.CharField(max_length=255, blank=True)
    manufacturer=models.CharField(max_length=255)
    sell_price=models.FloatField(null=True, blank=True)

    class Meta:
        abstract = True

class Keyboard(CommonModel):
    size_choices = [
        ("Numpad", "Numpad"),
        ("40%", "40%"),
        ("60%", "60%"),
        ("65%", "65%"),
        ("75%", "75%"),
        ("TKL", "TKL"),
        ("1800", "1800"),
        ("Full", "Full"),
        ("Other", "Other"),
    ]

    wkl_choices = [
        ("Y", "Y"),
        ("N", "N"),
        ("N/A", "N/A"),
    ]

    size=models.CharField(max_length=255, choices=size_choices)
    color=models.CharField(max_length=255)
    pcb=models.CharField(max_length=255)
    plate=models.CharField(max_length=255)
    wkl=models.CharField(max_length=255, choices=wkl_choices)
    foam=models.CharField(max_length=255, blank=True)
    material=models.CharField(max_length=255, blank=True)
    front_height=models.FloatField(null=True, blank=True)
    typing_angle=models.FloatField(null=True, blank=True)
    mount=models.CharField(max_length=255, blank=True)
    weight=models.CharField(max_length=255, blank=True)
    knob=models.CharField(max_length=255, blank=True)
    extra_pcbs=models.CharField(max_length=255, blank=True)
    extra_plates=models.CharField(max_length=255, blank=True)
    extra_accessories=models.CharField(max_length=255, blank=True)

    def get_absolute_url(self):
        return super().get_absolute_url("keyboard")

class Keycap(CommonModel):
    production_choices = [
        ("Doubleshot", "Doubleshot"),
        ("Tripleshot", "Tripleshot"),
        ("Dye-Sublimated", "Dye-Sublimated"),
        ("Other", "Other"),
    ]

    profile=models.CharField(max_length=255)
    sets=models.CharField(max_length=255)
    material=models.CharField(max_length=255)
    production=models.CharField(max_length=255, choices=production_choices)

    def get_absolute_url(self):
        return super().get_absolute_url("keycap")

class Switch(CommonModel):
    switch_type_choices = [
        ("Linear", "Linear"),
        ("Tactile", "Tactile"),
        ("Clicky", "Clicky"),
    ]

    switch_type=models.CharField(max_length=255, choices=switch_type_choices)
    lube=models.CharField(max_length=255, blank=True)
    film=models.CharField(max_length=255, blank=True)
    actuation_force=models.FloatField(null=True, blank=True)
    bottom_out_force=models.FloatField()
    top_material=models.CharField(max_length=255, blank=True)
    bottom_material=models.CharField(max_length=255, blank=True)
    stem_material=models.CharField(max_length=255, blank=True)
    spring_material=models.CharField(max_length=255, blank=True)
    spring_length=models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ['-name']
        verbose_name_plural = "switches"

    def get_absolute_url(self):
        return super().get_absolute_url("switch")

class Build(BaseCommonModel):
    keyboard=models.ForeignKey(Keyboard, on_delete=models.CASCADE)
    keycap=models.ForeignKey(Keycap, on_delete=models.CASCADE)
    switch=models.ForeignKey(Switch, on_delete=models.CASCADE)

    @property
    def cost(self):
        return keyboard.cost + keycap.cost + switch.cost

    def get_absolute_url(self):
        return super().get_absolute_url("build")

class Artisan(CommonModel):
    build=models.ForeignKey(Build, on_delete=models.SET_NULL, blank=True, null=True)
    profile=models.CharField(max_length=255, blank=True)

    def get_absolute_url(self):
        return super().get_absolute_url("artisan")

class Accessory(CommonModel):
    class Meta:
        ordering = ['-name']
        verbose_name_plural = "accessories"

    def get_absolute_url(self):
        return super().get_absolute_url("accessory")
