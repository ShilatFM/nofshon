from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('kids', views.kids, name='kids'),
    path('details/<str:name>', views.details, name='details'),
]