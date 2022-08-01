from email.mime import image
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10)
    image = models.FileField(upload_to='profile/')
    city = models.ForeignKey('City', related_name='user_city', on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__ (self):
        return str(self.name)
