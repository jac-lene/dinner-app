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
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Chat(models.Model):
    subject = models.CharField(max_length=200)
    dinner = models.ManyToOneRel()
    userName = models.OneToOneField()
    hostName = models.OneToOneField()

    def __str__(self):
        return self.name

class Message(models.Model):
    text = models.TextField()
    time = models.DateTimeField()
    userName = models.OneToOneField()
    hostName = models.OneToOneField()

    def __str__(self):
        return self.name

class Dinner(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    time = models.DateTimeField()
    attendees = models.ManyToOneRel()
    location = models.TextField()
    capacity = models.IntegerField(max_length=2)
    isPublic = models.BooleanField()

    def __str__(self):
        return self.name
