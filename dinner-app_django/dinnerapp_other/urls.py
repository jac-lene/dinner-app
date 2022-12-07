from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.Users.as_view(), name="users"),
    path('users/<int:pk>', views.UserDetail.as_view(), name="user_detail"),
    path('register/', views.RegisterView.as_view(), name="auth_register"),
    path('profiles/', views.ProfileList.as_view(), name="profile_list"),
    path('profiles/<int:pk>/', views.ProfileDetail.as_view(), name="profile_detail"),
    path('dinners/', views.DinnerList.as_view(), name="dinner_list"),
    path('dinners/<int:dinnerId>/', views.DinnerShow.as_view(), name='dinner'),
    path('photos/', views.PhotoList.as_view(), name="photos_list"),
    path('chats/<int:userId>/', views.ChatList.as_view(), name="chat_list"),
    path('messages/<int:chatId>/', views.MessageList.as_view(), name="message_list"),
]
