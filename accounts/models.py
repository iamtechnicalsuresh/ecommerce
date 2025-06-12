from django.contrib.auth.models import AbstractUser
from django.conf import settings

from django.db import models

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        SELLER = 'SELLER', 'Seller'
        CUSTOMER = 'CUSTOMER', 'Customer'

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.CUSTOMER)
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Optional
    dob = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(
        upload_to="profile_photos/", null=True, blank=True
    )

    def is_seller(self):
        return self.role == self.Role.SELLER

    def is_customer(self):
        return self.role == self.Role.CUSTOMER

    def is_admin(self):
        return self.role == self.Role.ADMIN
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]  # Username still required for superuser creation




class CustomerProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.full_name