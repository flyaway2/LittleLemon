from django.shortcuts import render
from rest_framework import generics
from .models import Booking,Menu
from .serializers import MenuSerializer
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from rest_framework.permissions import IsAuthenticated
# Create your views here.

def index(request):
    return render(request,"index.html",{})

class MenuItemView(generics.ListCreateAPIView):
    queryset=Menu.objects.all()
    #permission_classes=[IsAuthenticated]
    serializer_class=MenuSerializer
    # def create(self, request):
    #     serializer=MenuSerializer(data=request.data)
    #     if serializer.is_valid():
    #         try:
    #             serializer.save()
    #             return Response(serializer,status=status.HTTP_200_OK)
    #         except IntegrityError:        
    #             return Response({"msg":"item already exist"},status=status.HTTP_400_BAD_REQUEST)
    #     else:
    #         return Response({"msg":"invalid data"},status=status.HTTP_400_BAD_REQUEST)
            
class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset=Menu.objects.all()
    serializer_class=MenuSerializer

            
        
    