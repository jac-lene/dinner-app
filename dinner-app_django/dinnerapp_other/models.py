from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    profileImage = models.TextField()
    bannerImage = models.TextField()
    pronouns = models.CharField(max_length=200)
    orientation = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    age = models.IntegerField(max_length=3)
    profession = models.CharField(max_length=200)
    about = models.TextField()
    city = models.CharField(max_length=200)
    isHost = models.BooleanField()
    dinners = models.ManyToOneRel()
    user = models.OneToOneField()

    def __str__(self):
        return self.name