
from urllib import response

from django.shortcuts import render
from rest_framework.response import Response
from .serializers import ProjectSerializer, ProjectImageSerializer
from .models import Project, ProjectImage
from rest_framework.views import APIView

# Create your views here.

class MyProjects(APIView):
    def get(self, request, fromat=None):
        projects= Project.objects.all()
        serializer= ProjectSerializer(projects,many=True)
        return Response(serializer.data)

class ProjectDetails(APIView):
    def get(self, request,slug , fromat=None):
        projects= Project.objects.get(slug=slug)
        serializer= ProjectSerializer(projects, many=False)
        return Response(serializer.data)
class ProjectImages(APIView):
    def get(self, request,project_slug, fromat=None):
        project_images= ProjectImage.objects.filter(Project__slug= project_slug)
        serializer= ProjectImageSerializer(project_images,many=True)
        return Response(serializer.data)
        

