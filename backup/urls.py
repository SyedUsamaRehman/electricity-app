from django.urls import path
from . import views

urlpatterns = [
    path('backup/', views.backup_database, name='backup_view'),
]