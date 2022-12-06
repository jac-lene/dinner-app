from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

class Profile(models.Model):
    pronouns = models.CharField(max_length=200)
    orientation = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    age = models.IntegerField()
    profession = models.CharField(max_length=200)
    about = models.TextField()
    city = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    isHost = models.BooleanField()

    def __str__(self):
        return self.name

class Photos(models.Model):
    isProfile = models.BooleanField()
    imgUrl = models.TextField()
    profile = models.ForeignKey(Profile, related_name='photos', on_delete=models.CASCADE)

class Dinner(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    time = models.DateTimeField()
    location = models.TextField()
    capacity = models.IntegerField()
    isPublic = models.BooleanField()
    host = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Chat(models.Model):
    subject = models.CharField(max_length=200)
    dinner = models.ForeignKey(Dinner, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Message(models.Model):
    text = models.TextField()
    time = models.DateTimeField()
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)

    def __str__(self):
        return self.name