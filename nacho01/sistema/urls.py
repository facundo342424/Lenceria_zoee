from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('productos/', views.productos, name='productos'),
    path('logout/', views.salir, name='salir'),
    path('perfil/', views.perfil, name='perfil'),
    path('register/', views.register, name='register'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html', success_url='password_change/done/'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
]
