from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rand', views.rand, name= 'random'),
]