import os
import tempfile

from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from PIL import Image


class ImageResizerTestCase(TestCase):
    @classmethod
    def setUp(cls) -> None:
        cls.temp_dir_obj = tempfile.TemporaryDirectory()
        cls.temp_dir = cls.temp_dir_obj.__enter__()

    @classmethod
    def tearDown(cls) -> None:
        cls.temp_dir_obj.__exit__(None, None, None)

    def test_resize_picture(self):
        temp_image_path = os.path.join(self.temp_dir, 'test_image.jpg')

        image = Image.new('RGB', (800, 600), (255, 255, 255))
        image.save(temp_image_path)

        with open(temp_image_path, 'rb') as file:
            uploaded_file = SimpleUploadedFile('test_image.jpg', file.read(), content_type='image/jpeg')

        response = self.client.post('/api/resize_picture/', {
            'file': uploaded_file,
            'width': 300,
            'height': 200
        })

        self.assertEqual(response.status_code, 200)
        self.assertIn('url', response.json())

        modified_image = Image.open(response.json()['url'])
        self.assertEqual(modified_image.format, 'JPEG')
        self.assertEqual(modified_image.width, 300)
        self.assertEqual(modified_image.height, 200)
        modified_image.close()

    def test_resize_picture_png(self):
        temp_image_path = os.path.join(self.temp_dir, 'test_image.png')

        image = Image.new('RGB', (800, 600), (255, 255, 255))
        image.save(temp_image_path)

        with open(temp_image_path, 'rb') as file:
            uploaded_file = SimpleUploadedFile('test_image.png', file.read(), content_type='image/png')

        response = self.client.post('/api/resize_picture/', {
            'file': uploaded_file,
            'width': 300,
            'height': 200
        })

        self.assertEqual(response.status_code, 200)
        self.assertIn('url', response.json())

        modified_image = Image.open(response.json()['url'])
        self.assertEqual(modified_image.format, 'PNG')
        self.assertEqual(modified_image.width, 300)
        self.assertEqual(modified_image.height, 200)
        modified_image.close()

    def test_resize_picture_without_height(self):
        temp_image_path = os.path.join(self.temp_dir, 'test_image.jpg')

        image = Image.new('RGB', (800, 600), (255, 255, 255))
        image.save(temp_image_path)

        with open(temp_image_path, 'rb') as file:
            uploaded_file = SimpleUploadedFile('test_image.jpg', file.read(), content_type='image/jpeg')

        response = self.client.post('/api/resize_picture/', {
            'file': uploaded_file,
            'width': 300,
        })

        self.assertEqual(response.status_code, 200)
        self.assertIn('url', response.json())

        modified_image = Image.open(response.json()['url'])
        self.assertEqual(modified_image.format, 'JPEG')
        self.assertEqual(modified_image.width, 300)
        self.assertEqual(modified_image.height, 225)
        modified_image.close()
