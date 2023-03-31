from django.urls import path
from .import views

urlpatterns = [

    path('register',views.schoolregisterView.as_view(),name='register'),
    path('login',views.loginView.as_view(),name='login'),
    path('studentlist',views.getstudentView.as_view(),name='studentlist'),
   
    path('updatestudent/<int:id>',views.updatestudentView.as_view(),name='updatestudent'),
   
]
