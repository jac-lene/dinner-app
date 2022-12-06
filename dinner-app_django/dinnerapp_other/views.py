from django.shortcuts import render
from django.http import JsonResponse
from .serializers import UserSerializer
from rest_framework.views import APIView
from .models import User

from .models import Profile, Dinner, Chat, Message, Photos
from .serializers import PhotosSerializer, ProfileSerializer, DinnerSerializer, ChatSerializer, MessageSerializer, UserSerializer
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
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class PhotoList(generics.ListCreateAPIView):
    queryset = Photos.objects.all()
    serializer_class = PhotosSerializer

class PhotoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Photos.objects.all()
    serializer_class = PhotosSerializer

class DinnerList(generics.ListCreateAPIView):
    queryset = Dinner.objects.all()
    serializer_class = DinnerSerializer

class DinnerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dinner.objects.all()
    serializer_class = DinnerSerializer

class ChatList(generics.ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

class ChatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

class MessageList(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer





