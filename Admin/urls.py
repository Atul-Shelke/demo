from django.urls import path,include
from .import views
urlpatterns = [
    
path('schoollist',views.schooldataView.as_view(),name='schhollist'),
path('filterdata',views.getfilterView.as_view(),name='filterdata'),
path('addgrades',views.gradesView.as_view(),name='addgrades')
]