from django.contrib import admin
from .models import Blog
from import_export.admin import ImportExportModelAdmin

class BlogModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'dop']
    ordering = ['-title']
    search_fields = ['title', 'author']
    list_filter = ['dop']
    list_per_page = 2
    list_editable = ['title']

admin.site.register(Blog, BlogModelAdmin)
