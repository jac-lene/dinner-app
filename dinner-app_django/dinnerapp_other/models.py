from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Profile(models.Model):
    pronouns = models.CharField(max_length=200)
    orientation = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    age = models.IntegerField()
    profession = models.CharField(max_length=200)
    bio = models.TextField()
    location = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    isHost = models.BooleanField(default=False)
    isVerified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name

class Location(models.Model):
    address = models.CharField(max_length=200)
    apartment = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip = models.CharField(max_length=5)
    country = models.CharField(max_length=200, default='United States')

    def __str__(self):
        return self.address

class Dinner(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    dateTime = models.DateTimeField()
    capacity = models.IntegerField()
    host = models.ForeignKey(Profile, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, default=1)
    houseRules = models.TextField(default='have fun')

    def __str__(self):
        return self.name


class Review(models.Model):
    body = models.TextField()
    subject = models.CharField(max_length=100)
    profile = models.ForeignKey(Profile, related_name='review', on_delete=models.CASCADE)
    dinner = models.ForeignKey(Dinner, related_name='review', on_delete=models.CASCADE)

    def __str__(self):
        return self.name 

class Photo(models.Model):
    isProfile = models.BooleanField()
    imgUrl = models.TextField()
    profile = models.ForeignKey(Profile, related_name='photo', on_delete=models.CASCADE)
    dinner = models.ForeignKey(Dinner, related_name='photo', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Chat(models.Model):
    subject = models.CharField(max_length=200)
    dinner = models.ForeignKey(Dinner, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.dinner.name + '-' + self.user.user.first_name

class Message(models.Model):
    text = models.TextField()
    time = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:60]