from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#from .models import Flashcard
from .serializers import UserProfileSerializer
from tablib import Dataset
from student.models import UserProfile

class UserProfileList(APIView):
    def get(self, request, phone_number):
        UserProfile1 =UserProfile.objects.filter(phone_number = phone_number)
        serializer=UserProfileSerializer(UserProfile1, many=True)
        return Response(serializer.data)

    def post(self):
        pass
