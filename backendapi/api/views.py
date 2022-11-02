from ast import Import
from email.policy import HTTP
from http.client import HTTPResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from api.models import deskStatus
from api.serializers import UserSerializer
from .serializers import StatusSerializer


from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class userViewSet(viewsets.ModelViewSet):
    queryset =User.objects.all()
    serializer_class = UserSerializer




@api_view(['GET'])
def ShowAll(request):
    status=deskStatus.objects.all()
    serializer=StatusSerializer(status,many=True)
    return Response(serializer.data)



@api_view(['GET'])
def Showsingle(request,pk):
    status=deskStatus.objects.get(desk_value=pk)
    serializer=StatusSerializer(status,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def Updatesingle(request,pk):
    status=deskStatus.objects.get(desk_value=pk)
    serializer=StatusSerializer(instance=status,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)