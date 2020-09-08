from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Staff, Profile

@receiver(post_save, sender=Staff)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(staff=instance)

@receiver(post_save, sender=Staff)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()