from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Project(models.Model): 
#model for your projects
    project_name=models.CharField(max_length=30)
    project_id=models.AutoField(primary_key=True)
    project_logo=models.CharField(max_length=100)
    date_created=models.DateTimeField(default=timezone.now())
    description=models.CharField(max_length=50)
    category=models.CharField(max_length=30)
    skills_reqd=models.CharField(max_length=100)
    edu_background_reqd=models.CharField(max_length=100)
    payment=models.IntegerField(default=0)
    status=models.CharField(max_length=15)

    def __str__(self):
        return self.project_name

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    
    # Override the __unicode__() method to return out something meaningful!
    def __str__(self):
        return self.user.username

class Profile(models.Model):
    user = models.ForeignKey(User)
    oauth_token = models.CharField(max_length=200)
    oauth_secret = models.CharField(max_length=200)

    def __str__(self):
        return self.user

class GoogleProfile(models.Model):
    user = models.ForeignKey(User)
    google_user_id = models.CharField(max_length=100)
    time_created = models.DateTimeField(auto_now_add=True)
    access_token = models.CharField(max_length=100)
    profile_url = models.CharField(max_length=100)

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)