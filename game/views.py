from dataclasses import dataclass
from urllib import request
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serializers import GameSerializer, GameImagesSerializer, GameSpecificationsSerializer
from .models import Game, GameImages, GameSpecifications


@api_view(['GET'])
def getAllTheGames(request):
    allGames = Game.objects.all()
    serializer = GameSerializer(allGames, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getSingleGame(request, pk=-1):
    singleGame = Game.objects.get(_id=pk)
    serializer = GameSerializer(singleGame, many=False)
    return Response(serializer.data)
