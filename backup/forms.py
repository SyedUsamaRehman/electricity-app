from django import forms
from .models import Backup

class BackupForm(forms.ModelForm):
    class Meta:
        model = Backup
        fields = ['backup_name', 'backup_date', 'description']  # Adjust fields as per your Backup model
        widgets = {
            'backup_name': forms.TextInput(attrs={'class': 'form-control'}),
            'backup_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }