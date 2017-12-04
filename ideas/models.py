from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

"""
User Info:
    username
    password
    email
    first_name
    last_name
"""

class Profile(models.Model):
    joined = models.DateField(default=datetime.date.today)
    #rep is total
    reputation = models.IntegerField(default=0)
    #weight
    weight = models.IntegerField(default=1)
    bio = models.TextField(blank=True)
    email = models.EmailField(blank=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    #user.profile.stuff
    #Create Profile on creation of user
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return self.user.username

class Post(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateField(default=datetime.date.today)
    points = models.IntegerField(default=0)
    content = models.TextField()
    mods = models.ManyToManyField(Profile)

    def __str__(self):
        return self.title

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


class Comment(models.Model):
    text = models.TextField()
    points = models.IntegerField(default = 0)
    parent_post = models.ForeignKey(Post, null=True)
    parent_comment = models.ForeignKey('self', null=True)
    commenter = models.ForeignKey(Profile, null=True)

    def __str__(self):
        return self.commenter.user.username
