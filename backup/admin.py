from django.contrib import admin
from .models import Backup

@admin.register(Backup)
class BackupAdmin(admin.ModelAdmin):
    list_display = ('id', 'backup_date', 'file_name', 'file_size')
    search_fields = ('file_name',)
    ordering = ('-backup_date',)

    def file_name(self, obj):
        return obj.file_name

    def file_size(self, obj):
        return obj.file_size