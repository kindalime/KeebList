from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import *
from django.views.generic import *
from django.db.models import Sum
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import *
from .forms import *

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

class AccessoryCreateView(CommonCreateView):
    model = Accessory
    fields = "__all__"

class AccessoryUpdateView(CommonUpdateView):
    model = Accessory

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

class ArtisanCreateView(CommonCreateView):
    model = Artisan
    form_class = ArtisanForm

    def get_initial(self):
        return super().get_initial(self.request, Artisan)

class ArtisanUpdateView(CommonUpdateView):
    model = Artisan

class ArtisanDeleteView(CommonDeleteView):
    model = Artisan
    success_url = reverse_lazy('artisan')

class BuildListView(CommonListView):
    pass

class BuildDetailView(CommonDetailView):
    pass

class BuildCreateView(CommonCreateView):
    pass

class BuildUpdateView(CommonUpdateView):
    pass

class BuildDeleteView(CommonDeleteView):
    pass

class KeyboardListView(CommonListView):
    pass

class KeyboardDetailView(CommonDetailView):
    pass

class KeyboardCreateView(CommonCreateView):
    pass

class KeyboardUpdateView(CommonUpdateView):
    pass

class KeyboardDeleteView(CommonDeleteView):
    pass

class KeycapListView(CommonListView):
    pass

class KeycapDetailView(CommonDetailView):
    pass

class KeycapCreateView(CommonCreateView):
    pass

class KeycapUpdateView(CommonUpdateView):
    pass

class KeycapDeleteView(CommonDeleteView):
    pass

class SwitchListView(CommonListView):
    pass

class SwitchDetailView(CommonDetailView):
    pass

class SwitchCreateView(CommonCreateView):
    pass

class SwitchUpdateView(CommonUpdateView):
    pass

class SwitchDeleteView(CommonDeleteView):
    pass