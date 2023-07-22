
from django.urls import path
from admissions.views import admissions

urlpatterns = [
  
    path('admissions/',admissions),
   

]
