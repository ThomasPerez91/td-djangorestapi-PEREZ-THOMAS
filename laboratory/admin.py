from django.contrib import admin
from .models import Researcher, Project, Publication

admin.site.register(Researcher)
admin.site.register(Project)
admin.site.register(Publication)
