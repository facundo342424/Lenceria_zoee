from django.urls import path
from .views import ClienteListView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView

urlpatterns = [
    path('api/clientes/', ClienteListView.as_view(), name='api_clientes'),
    path('clientes/add/', ClienteCreateView.as_view(), name='cliente_add'),
    # path('clientes/edit/<int:pk>/', ClienteUpdateView.as_view(), name='cliente_edit'),
    # path('clientes/delete/<int:pk>/', ClienteDeleteView.as_view(), name='cliente_delete'),
]
