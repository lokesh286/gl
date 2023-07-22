from django.urls import path
from finance.views import money

urlpatterns = [
  
    path('money/',money),
   

]