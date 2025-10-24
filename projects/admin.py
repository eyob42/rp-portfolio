from django.contrib import admin
from .models import Projects

class ProjectAdmin(admin.ModelAdmin):
    pass


admin.site.register(Projects, ProjectAdmin)