from dataclasses import fields
from rest_framework import serializers
from .models import Project, ProjectImage
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project

        fields= (
            "ProjectName",
            "image_url",
            "id",
            "slug",
            "description",
            "source_code",
            "website",

            )

class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ProjectImage

        fields=(
            "Project",
            "Image",
            'image_url',
            "id",
        )

