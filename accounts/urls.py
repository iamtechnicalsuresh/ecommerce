from django.urls import path
from .views import customer_register, login_view, logout_view

urlpatterns = [
    path('register/', customer_register, name='customer-register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]