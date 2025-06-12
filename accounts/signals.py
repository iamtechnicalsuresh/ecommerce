from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, CustomerProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == User.Role.CUSTOMER:
        CustomerProfile.objects.create(user=instance)
