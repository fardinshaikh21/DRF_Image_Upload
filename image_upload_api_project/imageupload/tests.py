from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

class ImageUploadAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_upload_image(self):
        url = reverse('upload_image')
        with open('path/to/your/image.jpg', 'rb') as image_file:
            response = self.client.post(url, {'image': image_file}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)