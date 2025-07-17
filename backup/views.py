from django.shortcuts import render
from django.http import HttpResponse
import os
import shutil
from django.conf import settings
from datetime import datetime

def backup_database(request):
    if request.method == "POST":
        # Define the backup directory and filename
        backup_dir = os.path.join(settings.BASE_DIR, 'backups')
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_file = os.path.join(backup_dir, f'database_backup_{timestamp}.sqlite3')

        # Copy the database file to the backup location
        shutil.copy(settings.DATABASES['default']['NAME'], backup_file)

        return HttpResponse(f"Backup created successfully: {backup_file}")

    return render(request, 'backup/backup.html')