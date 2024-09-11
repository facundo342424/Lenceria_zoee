# urls.py
# urls.py
from django.urls import path
from Productos.views import ProductListView, ProductCreateView, ProductDeleteView

urlpatterns = [
    path('', ProductListView.as_view(), name='productos-list'),
    path('add/', ProductCreateView.as_view(), name='productos-add'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='productos-delete'),
]



