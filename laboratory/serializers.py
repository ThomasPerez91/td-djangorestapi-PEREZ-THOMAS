from rest_framework import serializers  # type: ignore
from .models import Researcher, Project, Publication


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    publications = PublicationSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'


class ResearcherSerializer(serializers.ModelSerializer):
    led_projects = ProjectSerializer(many=True, read_only=True)
    projects = serializers.PrimaryKeyRelatedField(
        queryset=Project.objects.all(), many=True, allow_null=True, required=False)

    class Meta:
        model = Researcher
        fields = '__all__'
