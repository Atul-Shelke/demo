from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .serializers import schoolSerializer,studentSerializer,gradesSerializer
from schools.models import schoolregister
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework import generics
from students.models import student
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.

class schooldataView(APIView):
    authentication_classes=[JWTAuthentication]
    def get(self,request):
        sc=schoolregister.objects.all()
        serializer=schoolSerializer(sc,many=True)

        return Response({
            'status':200,
            'msg':'Onboarded listing school',
            'data':serializer.data
        },status=status.HTTP_200_OK)
    
class getfilterView(generics.ListAPIView):
   
     authentication_classes=[JWTAuthentication] 
     queryset = student.objects.all()
     serializer_class =studentSerializer
     filter_backends = [DjangoFilterBackend]
     filterset_fields = ['grades','school']

class gradesView(APIView):
    def post(self,request):
        serializer=gradesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status':200,
                'msg':'Grades created successfully',
                'data':serializer.data
            },status=status.HTTP_200_OK)
        
        else:
            return Response({
                'status':400,
                'msg':'something went wrong',
                'data':serializer.errors
            },status=status.HTTP_400_BAD_REQUEST)