from dataclasses import dataclass
from urllib import request
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import CartSerializer
from .models import Cart


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserCartGames(request):
    cartGames = Cart.objects.filter(user=request.user)
    serializer = CartSerializer(cartGames, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteGameFromUsersCart(request, pk=-1):
    cartGame = Cart.objects.filter(user=request.user, _id=pk)
    cartGame.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addGameToUserCart(request):
    print(request.data)
    print(request.user.id)
    serializer = CartSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUserCart(request, pk=-1):
    currentCartGames = Cart.objects.filter(
        user=request.user, _id=pk)
    newCartGames = CartSerializer(
        instance=currentCartGames, newCartGames=request.data)
    if newCartGames.is_valid():
        newCartGames.save()
        return Response(newCartGames.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
