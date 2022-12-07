from django.urls import path
from . import views

urlpatterns = [
    path('', views.Users.as_view(), name="users"),
    path('profiles/', views.ProfileList.as_view(), name="profile_list"),
    path('profiles/<int:pk>/', views.ProfileDetail.as_view(), name="profile_detail"),
    path('dinners/', views.DinnerList.as_view(), name="dinner_list"),
    path('dinners/<int:dinnerId>/', views.DinnerShow.as_view(), name='dinner'),
    path('photos/', views.PhotoList.as_view(), name="photos_list"),
    path('chats/<int:userId>/', views.ChatList.as_view(), name="chat_list"),
    path('messages/<int:chatId>/', views.MessageList.as_view(), name="message_list"),
]
