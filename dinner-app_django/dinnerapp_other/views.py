from django.shortcuts import render
from django.http import JsonResponse
from .serializers import UserSerializer
from rest_framework.views import APIView
from .models import User

from .models import Profile, Dinner, Chat, Message
from .serializers import ProfileSerializer, DinnerSerializer, ChatSerializer, MessageSerializer, UserSerializer, RegisterSerializer, MyTokenObtainPairSerializer
from rest_framework import generics, status
from rest_framework_simplejwt.views import TokenObtainPairView


class Users(APIView):
    def get(self, request):
        data = User.objects.all()
        serializer = UserSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

class UserDetail(APIView):
    def get_user_auth(self, id):
        return User.objects.all().filter(id=id)

    def get_user_profile(self, id):
        return Profile.objects.all().filter(user_id=id)

    def get(self, request, pk):
        user = UserSerializer(self.get_user_auth(pk), many=True)
        profile = ProfileSerializer(self.get_user_profile(pk), many=True)
        return JsonResponse({"user": user.data, "profile": profile.data}, safe=False)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = ([])
    serializer_class = RegisterSerializer

class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    def get(self, request, pk):
        data = Profile.objects.filter(pk=pk)
        serializer = ProfileSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

class DinnerList(generics.ListCreateAPIView):
    def get(self, request):
        data = Dinner.objects.all()
        serializer = DinnerSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

class DinnerShow(generics.ListCreateAPIView):
    def get(self, request, dinnerId):
        data = Dinner.objects.filter(pk=dinnerId)
        serializer = DinnerSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

class AllChats(APIView):
    def get(self, request, userId):
        data = Chat.objects.filter(users=userId)
        serializer = ChatSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

class ChatList(APIView):
     def get(self, request, dinnerId):
        data = Chat.objects.filter(dinner=dinnerId)
        serializer = ChatSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

class MessageList(generics.ListCreateAPIView):
    def get(self, request, chatId):
        data = Message.objects.filter(chat=chatId)
        serializer = MessageSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)






