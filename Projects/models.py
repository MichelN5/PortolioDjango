from pyexpat import model
from unittest.util import _MAX_LENGTH
from xml.dom.minidom import ReadOnlySequentialNamedNodeMap
from django.db import models

# Create your models here.


class Project(models.Model):
    ProjectName= models.CharField(max_length=255)
    ProjectPic= models.ImageField()
    slug= models.CharField(max_length=255)
    description= models.TextField()
    source_code= models.CharField(max_length=255)
    website= models.CharField(max_length=255)
    def image_url(self):
        return "http://127.0.0.1:8000" + self.ProjectPic.url

    def __str__(self):
        return self.ProjectName


class ProjectImage(models.Model): 
    Project = models.ForeignKey(Project, related_name='project_image', on_delete=models.CASCADE)
    Image= models.ImageField()

    def image_url(self):
        return "http://127.0.0.1:8000" + self.Image.url

    def __str__(self):
        return f"{self.Project} | {self.Image.name}"
