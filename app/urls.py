from django.urls import path
from views import *

urlpatterns = [
    path('', index, name='index'),
    path('user/', user, name='user'),
]

urlpatterns += [
    path('book/', views.BookListView.as_view(), name='book'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('author/add/', AuthorCreateView.as_view(), name='author-add'),
    path('author/<int:pk>/', AuthorUpdateView.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author-delete'),
]