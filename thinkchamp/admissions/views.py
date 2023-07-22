from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def admissions(request):
    return HttpResponse("admissions data")

