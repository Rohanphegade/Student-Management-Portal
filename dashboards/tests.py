from django.test import TestCase
from django.urls import reverse
from student.models import Student

class DashboardTests(TestCase):
    def test_dashboard_home_status_code(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_documents_status_code(self):
        response = self.client.get(reverse('dashboard_documents'))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_accounts_status_code(self):
        # Create a dummy student to avoid division by zero error if any logic depends on it
        Student.objects.create(
            full_name="Test Student",
            email="test@test.com",
            phone="1234567890",
            course_name="Test Course",
            total_fees=1000,
            paid_fees=500,
            admission_date="2023-01-01"
        )
        response = self.client.get(reverse('dashboard_accounts'))
        self.assertEqual(response.status_code, 200)
