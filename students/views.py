from django.shortcuts import render
from rest_framework import status
from .serializers import studentserializer
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .models import student
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken
# Create your views here.

class studentView(APIView):
    def post(self,request):
        serializer=studentserializer(data=request.data,many=True)
        if serializer.is_valid():
            serializer.save()

            return Response({
                'status':200,
                'msg':'student account successfully created',
                'data':serializer.data
            },status=status.HTTP_200_OK)
        
        else:
            return Response({
                'status':400,
                'msg':'something went wrong',
                'data':serializer.errors
            },status=status.HTTP_400_BAD_REQUEST)
        
class studentloginView(APIView):
    def post(self,request):
        username=request.data.get('username')
        password=request.data.get('password')

        user=student.objects.filter(username=username,password=password).exists()
        
        
        if user==True:

            return Response({
                'status':200,
                
                'msg':'student login successfully'
            },status=status.HTTP_200_OK)
        
        else:

            return Response({
                'status':400,
                'msg':'Invalid Credentials'
            })
        
class updatestudentView(APIView):
    def put(self,request,id):
        stu=student.objects.get(id=id)
        serializer=studentserializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({
                'status':200,
                'msg':'student record updated successfully',
                'data':serializer.data
            },status=status.HTTP_200_OK)
        
        else:
            return Response({
                'status':400,
                'msg':'something went wrong',
                'data':serializer.errors
            },status=status.HTTP_400_BAD_REQUEST)
        