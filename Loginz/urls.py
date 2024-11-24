from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.inicio, name='inicio'),
    path('inicio', views.inicio, name='inicio'),
    path('productos/', views.productos, name='productos'),
    path('logout/', views.salir, name='salir'),
    path('perfil/', views.perfil, name='perfil'),
    path('register/', views.register, name='register'),
    path('password_reset_form/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html',
    email_template_name='registration/password_reset_email.html',subject_template_name='registration/password_reset_subject.txt',
    ), name='password_reset'), 
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html' ), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html',), name='password_reset_confirm'), 
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html',
    ), name='password_reset_complete'),
    path('superuser_dashboard/', views.superuser_dashboard, name='superuser_dashboard'),
    path('Gestion_Admin/',views.Gestion_Admin,name='Gestion_Admin'),
    path('estadistica/',views.estadistica,name='estadistica'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('stats_dashboard/', views.stats_dashboard, name='stats_dashboard'),
]