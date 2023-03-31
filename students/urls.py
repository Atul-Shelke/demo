from django.urls import path
from .import views
urlpatterns = [

  path('addstudent',views.studentView.as_view(),name='addstudent') ,
  path('login',views.studentloginView.as_view(),name='login'),
  path('updatestudent/<int:id>',views.updatestudentView.as_view(),name='updatestudent')
]
