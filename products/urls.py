from django.urls import path
from .views import products_view

urlpatterns = [
    path('register/', products_view, name='home'),
]