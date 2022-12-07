from django.shortcuts import render
from django.http import JsonResponse
from .serializers import UserSerializer
from rest_framework.views import APIView
from .models import User

from .models import Profile, Dinner, Chat, Message, Photo
from .serializers import PhotoSerializer, ProfileSerializer, DinnerSerializer, ChatSerializer, MessageSerializer, UserSerializer
from rest_framework import generics, status



class Users(APIView):
    def get(self, request):
        data = User.objects.all()
        serializer = UserSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    def get(self, request, pk):
        data = Profile.objects.filter(pk=pk)
        serializer = ProfileSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

class PhotoList(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

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

class ChatList(APIView):
     def get(self, request, userId):
        data = Chat.objects.filter(user=userId)
        serializer = ChatSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

class MessageList(generics.ListCreateAPIView):
    def get(self, request, chatId):
        data = Message.objects.filter(chat=chatId)
        serializer = MessageSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)






