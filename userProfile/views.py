from urllib import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Profile
from .serializers import ProfileSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    profile = Profile.objects.filter(user=request.user)
    serializer = ProfileSerializer(profile, many = False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addUserProfile(request):
    serializer = ProfileSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUserProfile(request, pk=-1):
    currentProfile = Profile.objects.filter(user = request.user, _id=pk)
    newProfile = ProfileSerializer(instance = currentProfile, newProfile = request.data)
    if newProfile.is_valid():
        newProfile.save()
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)