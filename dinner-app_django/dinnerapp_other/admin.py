from django.contrib import admin
from .models import Profile, Dinner, Message, Chat, Photo, Review, Location

# Register your models here.
admin.site.register(Profile)
admin.site.register(Dinner)
admin.site.register(Message)
admin.site.register(Chat)
admin.site.register(Photo)
admin.site.register(Review)
admin.site.register(Location)