from django.contrib import admin
from file.models import File
from import_export.admin import ImportExportModelAdmin


class FileAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    class FileAdmin(ImportExportModelAdmin):
        list_display = ('name', 'email', 'phone')

    admin.site.register(File)
