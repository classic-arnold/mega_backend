from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from django.contrib.auth.models import User
from core.models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    
@receiver(pre_save, sender=User)
def save_username(sender, instance, **kwargs):
	if instance.username is None:
		instance.username = instance.email