from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class User(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('C', 'Custom'),
    ]
    name = models.CharField(_('Name of User'), blank=True, max_length=50)
    profile_photo = models.ImageField(blank=True, upload_to='uploads/%Y/%m/%d')
    website = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    email = models.CharField(blank=True, max_length=50)
    phone_number = models.CharField(blank=True, max_length=50)
    gender = models.CharField(blank=True, choices=GENDER_CHOICES, max_length=50)
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    
    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
    