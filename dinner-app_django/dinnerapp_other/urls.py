from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [
    path('users/', views.Users.as_view(), name="users"),
    path('users/<int:pk>', views.UserDetail.as_view(), name="user_detail"),
    path('register/', views.RegisterView.as_view(), name="auth_register"),
    path('token/', views.MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('token/refresh/', views.TokenRefreshView.as_view(), name="token_refresh"),
    path('profiles/', views.ProfileList.as_view(), name="profile_list"),
    path('profiles/<int:pk>/', views.ProfileDetail.as_view(), name="profile_detail"),
    path('dinners/', views.DinnerList.as_view(), name="dinner_list"),
    path('dinners/<int:dinnerId>/', views.DinnerShow.as_view(), name='dinner'),
    path('allchats/<int:userId>/', views.AllChats.as_view(), name="all_chats"),
    path('chats/<int:dinnerId>/', views.ChatList.as_view(), name="chat_list"),
    path('messages/<int:chatId>/', views.MessageList.as_view(), name="message_list"),
]
