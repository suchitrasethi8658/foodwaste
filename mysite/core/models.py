from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .choices import * 


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    email = models.CharField(max_length=30, blank=True)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class Book(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    weight = models.IntegerField()
    locations = models.CharField(max_length=200)
    allocation = models.CharField(max_length=200)
    document = models.FileField(upload_to='documents/')

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('update_det', kwargs={'pk': self.pk})
		
class Orphanagedetails(models.Model):
    id = models.AutoField(primary_key=True)
    oname = models.CharField(max_length=200)
    olocation = models.CharField(max_length=200)
    totalppl = models.CharField(max_length=200)
    omobile = models.IntegerField()

    def __unicode__(self):
        return self.oname
     
    def get_absolute_url(self):
        return reverse('update_orp_det', kwargs={'pk': self.pk})