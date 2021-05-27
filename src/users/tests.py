from django.urls import reverse
from rest_framework import status

from core.tests import InitClass


class TestCustomerRegistration(InitClass):
    def setUp(self) -> None:
        self.user, self.user_client = self.create_user()
        self.anon_client = self.anon_client()
        self.super_user, self.superuser_client = self.create_super_user()

    def test_get(self):
        response = self.user_client.get(reverse('create_user'))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_post(self):
        data = {
            "email": self.fake.email(),
            "password": 'Aa#12312300',
            "password2": 'Aa#12312300',

        }
        response = self.user_client.post(reverse('create_user'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_change_password(self):
        data = {
            "old_password": "PaSwOrD123",
            "new_password": "Newpassword123#",
            "new_password2": "Newpassword123#"
        }
        response = self.user_client.put(reverse('change_pass'), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'success')
