from django.db import models
from django.contrib.auth.models import User


class Researcher(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    projects = models.ManyToManyField(
        'Project', related_name='researchers', blank=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    expected_end_date = models.DateField()
    project_leader = models.ForeignKey(
        Researcher, on_delete=models.CASCADE, related_name='led_projects', blank=True)

    def __str__(self):
        return self.title


class Publication(models.Model):
    title = models.CharField(max_length=200)
    abstract = models.TextField()
    associated_project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='publications')
    publication_date = models.DateField()

    def __str__(self):
        return self.title
