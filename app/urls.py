from django.urls import include, path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('user/', user, name='user'),
    path('signup/', SignUpView.as_view(), name='signup'),
]

urlpatterns += [
    path('accessory/', AccessoryListView.as_view(), name='accessory'),
    path('accessory/<slug:slug>', AccessoryDetailView.as_view(), name='accessory-detail'),
    path('accessory/create/', AccessoryCreateView.as_view(), name='accessory-create'),
    path('accessory/<slug:slug>/update/', AccessoryUpdateView.as_view(), name='accessory-update'),
    path('accessory/<slug:slug>/delete/', AccessoryDeleteView.as_view(), name='accessory-delete'),
]

urlpatterns += [
    path('artisan/', ArtisanListView.as_view(), name='artisan'),
    path('artisan/<slug:slug>', ArtisanDetailView.as_view(), name='artisan-detail'),
    path('artisan/create/', ArtisanCreateView.as_view(), name='artisan-create'),
    path('artisan/<slug:slug>/update/', ArtisanUpdateView.as_view(), name='artisan-update'),
    path('artisan/<slug:slug>/delete/', ArtisanDeleteView.as_view(), name='artisan-delete'),
]

urlpatterns += [
    path('build/', BuildListView.as_view(), name='build'),
    path('build/<slug:slug>', BuildDetailView.as_view(), name='build-detail'),
    path('build/create/', BuildCreateView.as_view(), name='build-create'),
    path('build/<slug:slug>/update/', BuildUpdateView.as_view(), name='build-update'),
    path('build/<slug:slug>/delete/', BuildDeleteView.as_view(), name='build-delete'),
]

urlpatterns += [
    path('keycap/', KeycapListView.as_view(), name='keycap'),
    path('keycap/<slug:slug>', KeycapDetailView.as_view(), name='keycap-detail'),
    path('keycap/create/', KeycapCreateView.as_view(), name='keycap-create'),
    path('keycap/<slug:slug>/update/', KeycapUpdateView.as_view(), name='keycap-update'),
    path('keycap/<slug:slug>/delete/', KeycapDeleteView.as_view(), name='keycap-delete'),
]

urlpatterns += [
    path('keyboard/', KeyboardListView.as_view(), name='keyboard'),
    path('keyboard/<slug:slug>', KeyboardDetailView.as_view(), name='keyboard-detail'),
    path('keyboard/create/', KeyboardCreateView.as_view(), name='keyboard-create'),
    path('keyboard/<slug:slug>/update/', KeyboardUpdateView.as_view(), name='keyboard-update'),
    path('keyboard/<slug:slug>/delete/', KeyboardDeleteView.as_view(), name='keyboard-delete'),
]

urlpatterns += [
    path('switch/', SwitchListView.as_view(), name='switch'),
    path('switch/<slug:slug>', SwitchDetailView.as_view(), name='switch-detail'),
    path('switch/create/', SwitchCreateView.as_view(), name='switch-create'),
    path('switch/<slug:slug>/update/', SwitchUpdateView.as_view(), name='switch-update'),
    path('switch/<slug:slug>/delete/', SwitchDeleteView.as_view(), name='switch-delete'),
]