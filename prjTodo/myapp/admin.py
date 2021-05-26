from django.contrib import admin
from .models import Task
from import_export.admin import ImportExportModelAdmin

class TaskModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'createdBy']
    ordering = ['-id']
    search_fields = ['name', 'createdBy']

admin.site.register(Task, TaskModelAdmin)
