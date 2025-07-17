from django.db import models

class Backup(models.Model):
    backup_date = models.DateTimeField(auto_now_add=True)
    backup_file = models.FileField(upload_to='backups/')
    file_name = models.CharField(max_length=255)
    file_size = models.IntegerField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Backup on {self.backup_date.strftime('%Y-%m-%d %H:%M:%S')}"