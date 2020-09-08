from django.shortcuts import render, redirect
from django.http import HttpResponse

# Django Rest imports
from rest_framework import viewsets
from .serializers import BloggerSerializer
from .models import Blogger

# Create your views here.

def index(request):
    return render(request, 'index.html')


def mydetails(request):
    return render(request, 'mydetails.html')



# Rest framework code
class BloggerViewSet(viewsets.ModelViewSet):
    queryset = Blogger.objects.all()
    serializer_class = BloggerSerializer