from django.shortcuts import render
from rest_framework import status
from .serializers import schoolregisterSerializer,studentSerializer
from rest_framework.decorators import APIView,authentication_classes,permission_classes
from rest_framework.response import Response
from .models import schoolregister
from students.models import student
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
# Create your views here.

class schoolregisterView(APIView):
   
    def post(self,request):
        serializer=schoolregisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({
                'status':200,
                'msg':'School created successfully',
                'data':serializer.data
            },status=status.HTTP_200_OK)
    
        else:
            return Response({
                'status':400,
                'msg':'something went wrong',
                'data':serializer.errors
            })
        
class loginView(APIView):
    def post(self,request):
        email=request.data.get('email')
        password=request.data.get('password')

        student=schoolregister.objects.get(email=email,password=password)

        if student:
            access = AccessToken.for_user(student)
            refresh = RefreshToken.for_user(student)
            student.access =access
            student.refresh = refresh  
            student.save()             

            return Response({
                'status':200,
                'refresh':str(refresh),
                'access':str(access),
                'msg':'school login successfully',
            },status=status.HTTP_200_OK)
            
        else:

            return Response({
                'status':400,
                'msg':'Invalid Credentials'
            },status=status.HTTP_400_BAD_REQUEST)
        
class getstudentView(APIView):
    def get(self,request):

        if request.GET.get('grades'):
            grades = request.GET.get('grades')
            students_list=student.objects.filter(grades = grades)
        else:
            students_list=student.objects.all()

        serializer=studentSerializer(students_list,many=True)

        return Response({
            'status':200,
            'msg':'All students Details',
            'data':serializer.data
        },status=status.HTTP_200_OK)
    

     

class updatestudentView(APIView):

    def put(self,request,id):
        stu=student.objects.get(id=id)
        serializer=studentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({
                'status':200,
                'msg':'Student Record successfully updated',
                'data':serializer.data
            },status=status.HTTP_200_OK)
        else:
            return Response({
                'status':400,
                'msg':'something went wrong',
                'data':serializer.errors
            })
