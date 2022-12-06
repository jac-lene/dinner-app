from django.shortcuts import render
from django.http import JsonResponse
from .serializers import UserSerializer
from rest_framework.views import APIView
from .models import User, Chat

class Users(APIView):
    def get(self, request):
        data = User.objects.all()
        serializer = UserSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

class Chat(APIView):
    def get(self, request, userId, dinnerId):
        data = Chat.objects.filter(user=userId, dinner=dinnerId)
        serializer = UserSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)
