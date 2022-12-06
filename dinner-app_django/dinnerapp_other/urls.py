from django.urls import path
from . import views

urlpatterns = [
    path('', views.Users.as_view(), name="users"),
    path('allchats/<int:userId>/<int:dinnerId>', views.Chat.as_view(), name="chat"),
]
