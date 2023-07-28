from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import LoginLog, MyUser

MyUser = get_user_model()

@receiver(post_save, sender=MyUser)
def create_login_log(sender, instance, created, **kwargs):
    if created:
        user_type = "Admin" if instance.is_staff else "User"
        LoginLog.objects.create(user=instance, user_type=user_type)
