from django.urls import path
from .views import (indexView, register, register_rol,profile_view, about, contact, edit_profile_view,index_arrendatario,dashboard_arrendador)


urlpatterns = [
    path('', indexView, name='home'),
    path('accounts/register', register, name='register'),
    path('accounts/register_rol', register_rol, name='register_rol'),
    path('register_rol', register_rol, name='register_rol'),
    path('profile', profile_view, name='profile'),
    path('profile/edit/', edit_profile_view, name='edit_profile'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('index', index_arrendatario, name='index_arrendatario'),
    path('dashboard', dashboard_arrendador, name="dashboard_arrendador"),
]