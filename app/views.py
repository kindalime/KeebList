from django.db import models
from django.db.models import Q, Sum
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import *
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
import zipfile
import shutil
import os, io

def get_costs(user=None):
    models = [Artisan, Accessory, Keyboard, Keycap, Switch]
    cost = 0
    gain = 0

    for model in models:
        if user:
            cost_model = model.objects.filter(user=user).aggregate(Sum('cost'))['cost__sum']
            gain_model = model.objects.filter(user=user, status="Sold").aggregate(Sum('sell_price'))['sell_price__sum']
        else:
            cost_model = model.objects.aggregate(Sum('cost'))['cost__sum']
            gain_model = model.objects.filter(status="Sold").aggregate(Sum('sell_price'))['sell_price__sum']

        if cost_model:
            cost += cost_model
        if gain_model:
            gain += gain_model

    if user:
        cost_model = Keyboard.objects.filter(user=user).aggregate(Sum('stabilizer_cost'))['stabilizer_cost__sum']
    else:
        cost_model = Keyboard.objects.aggregate(Sum('stabilizer_cost'))['stabilizer_cost__sum']

    if cost_model:
        cost += cost_model
    if gain_model:
        gain += gain_model

    return cost, cost - gain

def index(request):
    costs = get_costs()

    context = {
        'num_artisans': Artisan.objects.all().count(),
        'num_accessories': Accessory.objects.all().count(),
        'num_builds': Build.objects.all().count(),
        'num_keyboards': Keyboard.objects.all().count(),
        'num_keycaps': Keycap.objects.all().count(),
        'num_switches': Switch.objects.all().count(),
        'total_cost': costs[0],
        'net_cost': costs[1]
    }

    return render(request, 'index.html', context=context)

def user(request):
    user = request.user
    costs = get_costs(user=user)

    context = {
        'num_artisans': Artisan.objects.filter(user=user).count(),
        'num_accessories': Accessory.objects.filter(user=user).count(),
        'num_builds': Build.objects.filter(user=user).count(),
        'num_keyboards': Keyboard.objects.filter(user=user).count(),
        'num_keycaps': Keycap.objects.filter(user=user).count(),
        'num_switches': Switch.objects.filter(user=user).count(),
        'total_cost': costs[0],
        'net_cost': costs[1]
    }

    return render(request, 'user.html', context=context)

def report(request):
    model_list = [Artisan, Accessory, Build, Keyboard, Keycap, Switch]
    user = request.user
    os.mkdir("report")

    for model in model_list:
        objects = model.objects.filter(user=user)
        fields = []

        for field in model._meta.fields:
            if field.name not in ["id", "user"]:
                fields.append(field.name)
                if isinstance(field, models.OneToOneField) or isinstance(field, models.ForeignKey):
                    fields.append(f"{field.name} slug")

        with open(os.path.join("report", f"{model.__name__}.csv"), "w") as f:
            f.write(",".join(fields) + "\n")

            for obj in objects:
                data = []
                for field in model._meta.fields:
                    if field.name in ["id", "user"]:
                        continue                    
                    value = getattr(obj, field.name)
                    if value != 0 and not value:
                        value = ""

                    if hasattr(value, "slug"):
                        data.extend(value.name, value.slug)
                    else:
                        data.append(str(value))

                f.write(",".join(data) + "\n")

    outfile = io.BytesIO()
    with zipfile.ZipFile(outfile, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for model in model_list:
            zf.write(os.path.join("report", f"{str(model.__name__)}.csv"))
    value = outfile.getvalue()
    shutil.rmtree("report")

    response = HttpResponse(value, content_type="application/zip", headers={"Content-Disposition": 'attachment; filename="report.zip"'})
    return response

def duplicate_object(request, slug):
    models = [Artisan, Accessory, Keyboard, Keycap, Switch]
    for model in models:
        items = list(model.objects.filter(slug=slug))
        if len(items) > 0:
            item = items[0]
            break
    
    obj = copy.copy(item)
    obj.pk = None
    obj.slug = random_slug_string()
    obj._state.adding = True
    obj.save()
    return HttpResponseRedirect(obj.get_absolute_url())

class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    form_class = CustomUserCreationForm

class CorrectUserMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self, user):
        return self.request.user == user

class CommonListView(LoginRequiredMixin, ListView):
    def get_queryset(self, model, user):
        return model.objects.filter(user=user).filter(~Q(status="Sold"))

class CommonDetailView(CorrectUserMixin, DetailView):
    def test_func(self):
        return super().test_func(super().get_object().user)

    def get_context_data(self, model, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = super().get_object()
        data = []

        for field in model._meta.fields:
            if field.name in ["id", "user", "slug"]:
                continue

            name = field.name.replace("_", " ").title().replace("Pcb", "PCB")
            value = getattr(obj, field.name)
            if value != 0 and not value:
                value = ""
            data.append([name, value, hasattr(value, "get_absolute_url")])

        context['data'] = data
        return context

class CommonCreateView(LoginRequiredMixin, CreateView):
    def get_initial(self, request, model):
        initial = dict()
        for field in model._meta.fields:
            if field not in ["user", "id", "user_id"]:
                initial[field.name] = ""
        return initial

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CommonUpdateView(CorrectUserMixin, UpdateView):
    def test_func(self):
        return super().test_func(super().get_object().user)

class CommonDeleteView(CorrectUserMixin, DeleteView):
    def test_func(self):
        return super().test_func(super().get_object().user)

class AccessoryListView(CommonListView):
    model = Accessory
    template_name = 'models/accessory_list.html'
    context_object_name = 'accessory_list'

    def get_queryset(self):
        return super().get_queryset(Accessory, self.request.user)

class AccessoryDetailView(CommonDetailView):
    model = Accessory
    
    def get_context_data(self, **kwargs):
        return super().get_context_data(Accessory, **kwargs)

class AccessoryCreateView(CommonCreateView):
    model = Accessory
    form_class = AccessoryForm

    def get_initial(self):
        return super().get_initial(self.request, Accessory)

class AccessoryUpdateView(CommonUpdateView):
    model = Accessory
    form_class = AccessoryForm

class AccessoryDeleteView(CommonDeleteView):
    model = Accessory
    success_url = reverse_lazy('accessory')

class ArtisanListView(CommonListView):
    model = Artisan
    template_name = 'models/artisan_list.html'
    context_object_name = 'artisan_list'

    def get_queryset(self):
        return super().get_queryset(Artisan, self.request.user)

class ArtisanDetailView(CommonDetailView):
    model = Artisan
    
    def get_context_data(self, **kwargs):
        return super().get_context_data(Artisan, **kwargs)

class ArtisanCreateView(CommonCreateView):
    model = Artisan
    form_class = ArtisanForm

    def get_initial(self):
        return super().get_initial(self.request, Artisan)

class ArtisanUpdateView(CommonUpdateView):
    model = Artisan
    form_class = ArtisanForm

class ArtisanDeleteView(CommonDeleteView):
    model = Artisan
    success_url = reverse_lazy('artisan')

class BuildListView(CommonListView):
    model = Build
    template_name = 'models/build_list.html'
    context_object_name = 'build_list'

    def get_queryset(self):
        return Build.objects.filter(user=self.request.user)

class BuildDetailView(CommonDetailView):
    model = Build
    
    def get_context_data(self, **kwargs):
        return super().get_context_data(Build, **kwargs)

class BuildCreateView(CommonCreateView):
    model = Build
    form_class = BuildForm

    def get_initial(self):
        return super().get_initial(self.request, Build)

class BuildUpdateView(CommonUpdateView):
    model = Build
    form_class = BuildForm

class BuildDeleteView(CommonDeleteView):
    model = Build
    success_url = reverse_lazy('build')

class KeyboardListView(CommonListView):
    model = Keyboard
    template_name = 'models/keyboard_list.html'
    context_object_name = 'keyboard_list'

    def get_queryset(self):
        return super().get_queryset(Keyboard, self.request.user)

class KeyboardDetailView(CommonDetailView):
    model = Keyboard
    
    def get_context_data(self, **kwargs):
        return super().get_context_data(Keyboard, **kwargs)

class KeyboardCreateView(CommonCreateView):
    model = Keyboard
    form_class = KeyboardForm

    def get_initial(self):
        return super().get_initial(self.request, Keyboard)

class KeyboardUpdateView(CommonUpdateView):
    model = Keyboard
    form_class = KeyboardForm

class KeyboardDeleteView(CommonDeleteView):
    model = Keyboard
    success_url = reverse_lazy('keyboard')

class KeycapListView(CommonListView):
    model = Keycap
    template_name = 'models/keycap_list.html'
    context_object_name = 'keycap_list'

    def get_queryset(self):
        return super().get_queryset(Keycap, self.request.user)

class KeycapDetailView(CommonDetailView):
    model = Keycap
    
    def get_context_data(self, **kwargs):
        return super().get_context_data(Keycap, **kwargs)

class KeycapCreateView(CommonCreateView):
    model = Keycap
    form_class = KeycapForm

    def get_initial(self):
        return super().get_initial(self.request, Keycap)

class KeycapUpdateView(CommonUpdateView):
    model = Keycap
    form_class = KeycapForm

class KeycapDeleteView(CommonDeleteView):
    model = Keycap
    success_url = reverse_lazy('keycap')

class SwitchListView(CommonListView):
    model = Switch
    template_name = 'models/switch_list.html'
    context_object_name = 'switch_list'

    def get_queryset(self):
        return super().get_queryset(Switch, self.request.user)

class SwitchDetailView(CommonDetailView):
    model = Switch
    
    def get_context_data(self, **kwargs):
        return super().get_context_data(Switch, **kwargs)

class SwitchCreateView(CommonCreateView):
    model = Switch
    form_class = SwitchForm

    def get_initial(self):
        return super().get_initial(self.request, Switch)

class SwitchUpdateView(CommonUpdateView):
    model = Switch
    form_class = SwitchForm

class SwitchDeleteView(CommonDeleteView):
    model = Switch
    success_url = reverse_lazy('switch')
