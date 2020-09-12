from django.db.models.signals import post_save
from django.contrib.auth.models import User #user will be sender
from django.dispatch import receiver
from .models import Profile

#receiver function

@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def saveProfile(sender, instance, **kwargs):
        instance.profile.save()