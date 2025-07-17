from django.test import TestCase
from .models import Backup

class BackupModelTest(TestCase):
    def setUp(self):
        self.backup = Backup.objects.create(
            name="Test Backup",
            created_at="2023-10-01T12:00:00Z"
        )

    def test_backup_creation(self):
        self.assertEqual(self.backup.name, "Test Backup")
        self.assertIsNotNone(self.backup.created_at)

    def test_backup_str(self):
        self.assertEqual(str(self.backup), "Test Backup")