from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import *
from django.contrib.auth.mixins import LoginRequiredMixin
from models import *
from forms import *

def get_costs(user=None):
    models = [Artisan, Accessory, Keyboard, Keycap, Switch]
    cost = 0
    gain = 0

    for model in models:
        if user:
            cost += model.objects.filter(user=user).aggregate(Sum('cost'))
            gain += model.objects.filter(user=user).aggregate(Sum('sell_price'))
        else:
            cost += model.objects.all().aggregate(Sum('cost'))
            gain += model.objects.all().aggregate(Sum('sell_price'))
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


class CorrectUserMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self, user):
        return self.request.user == user

class CommonListView(LoginRequiredMixin, ListView):
    pass

class CommonDetailView(CorrectUserMixin, DetailView):
    def test_func(self):
        return super().test_func(super().get_object().user)

class CommonCreateView(LoginRequiredMixin, CreateView):
    pass

class CommonUpdateView(CorrectUserMixin, UpdateView):
    def test_func(self):
        return super().test_func(super().get_object().user)

class CommonDeleteView(CorrectUserMixin, DeleteView):
    success_url = reverse_lazy('author-list')

    def test_func(self):
        return super().test_func(super().get_object().user)
