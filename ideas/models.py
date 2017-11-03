from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

class Profile(models.Model):
    joined = models.DateField(default=datetime.date.today)
    #rep is total
    reputation = models.IntegerField()
    #weight
    weight = models.IntegerField()
    bio = models.TextField(blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #Create Profile on creation of user
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Post(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateField(default=datetime.date.today)
    points = models.IntegerField(default=0)
    content = models.TextField()

class Comment(models.Model):
    text = models.TextField()
    points = models.IntegerField(default = 0)
    
