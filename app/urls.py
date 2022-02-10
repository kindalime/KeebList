from django.urls import include, path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('user/', user, name='user'),
    path('signup/', SignUpView.as_view(), name='signup'),
]

urlpatterns += [
    path('accessory/', AccessoryListView.as_view(), name='accessory'),
    path('accessory/<int:pk>', AccessoryDetailView.as_view(), name='accessory-detail'),
    path('accessory/create/', AccessoryCreateView.as_view(), name='accessory-create'),
    path('accessory/<int:pk>/update/', AccessoryUpdateView.as_view(), name='accessory-update'),
    path('accessory/<int:pk>/delete/', AccessoryDeleteView.as_view(), name='accessory-delete'),
]

urlpatterns += [
    path('artisan/', ArtisanListView.as_view(), name='artisan'),
    path('artisan/<int:pk>', ArtisanDetailView.as_view(), name='artisan-detail'),
    path('artisan/create/', ArtisanCreateView.as_view(), name='artisan-create'),
    path('artisan/<int:pk>/update/', ArtisanUpdateView.as_view(), name='artisan-update'),
    path('artisan/<int:pk>/delete/', ArtisanDeleteView.as_view(), name='artisan-delete'),
]

urlpatterns += [
    path('build/', BuildListView.as_view(), name='build'),
    path('build/<int:pk>', BuildDetailView.as_view(), name='build-detail'),
    path('build/create/', BuildCreateView.as_view(), name='build-create'),
    path('build/<int:pk>/update/', BuildUpdateView.as_view(), name='build-update'),
    path('build/<int:pk>/delete/', BuildDeleteView.as_view(), name='build-delete'),
]

urlpatterns += [
    path('keycap/', KeycapListView.as_view(), name='keycap'),
    path('keycap/<int:pk>', KeycapDetailView.as_view(), name='keycap-detail'),
    path('keycap/create/', KeycapCreateView.as_view(), name='keycap-create'),
    path('keycap/<int:pk>/update/', KeycapUpdateView.as_view(), name='keycap-update'),
    path('keycap/<int:pk>/delete/', KeycapDeleteView.as_view(), name='keycap-delete'),
]

urlpatterns += [
    path('keyboard/', KeyboardListView.as_view(), name='keyboard'),
    path('keyboard/<int:pk>', KeyboardDetailView.as_view(), name='keyboard-detail'),
    path('keyboard/create/', KeyboardCreateView.as_view(), name='keyboard-create'),
    path('keyboard/<int:pk>/update/', KeyboardUpdateView.as_view(), name='keyboard-update'),
    path('keyboard/<int:pk>/delete/', KeyboardDeleteView.as_view(), name='keyboard-delete'),
]

urlpatterns += [
    path('switch/', SwitchListView.as_view(), name='switch'),
    path('switch/<int:pk>', SwitchDetailView.as_view(), name='switch-detail'),
    path('switch/create/', SwitchCreateView.as_view(), name='switch-create'),
    path('switch/<int:pk>/update/', SwitchUpdateView.as_view(), name='switch-update'),
    path('switch/<int:pk>/delete/', SwitchDeleteView.as_view(), name='switch-delete'),
]