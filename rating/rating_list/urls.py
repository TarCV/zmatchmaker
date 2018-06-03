from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('discipline/<int:id>/', views.discipline, name='disciplines'),
    path('player/<int:id>/', views.player, name='players'),
]
