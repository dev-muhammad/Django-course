from users.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class TestUserUpdateDeleteView(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_get_user(self):
        url = reverse('profile')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'testuser')

    def test_update_user(self):
        url = reverse('profile')
        response = self.client.put(url, {'username': 'newusername'}, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'newusername')

    def test_delete_user(self):
        url = reverse('profile')
        response = self.client.delete(url)
        self.user.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(self.user.is_active, False)
