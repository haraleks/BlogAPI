from django.urls import reverse
from rest_framework import status

from core.tests import InitClass


class TestBlogPost(InitClass):

    def setUp(self) -> None:
        self.user, self.user_client = self.create_user()
        self.anon_client = self.anon_client()
        self.super_user, self.superuser_client = self.create_super_user()
        self.blog_post = self.create_blog_post(self.user)
        self.url_pk = reverse('blogs_detail', args=[self.blog_post.pk])

    def test_get(self):
        response = self.user_client.get(reverse('blogs_post'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_anonim(self):
        response = self.anon_client.get(reverse('blogs_post'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrive(self):
        response = self.user_client.get(path=self.url_pk, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post(self):
        data = {
            "title": self.fake.text()[:19],
            "text": self.fake.text()
        }
        response = self.user_client.post(path=reverse('blogs_post'), data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_bad_request(self):
        data = {
            "title": self.fake.text(),
            "text": self.fake.text()
        }
        data2 = {
            "title": 'jksfjsf sfs 74343',
            "text": self.fake.text()
        }
        data3 = {
            "title": 'jksfjsf sfs ####',
            "text": self.fake.text()
        }
        response = self.user_client.post(path=reverse('blogs_post'), data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response = self.user_client.post(path=reverse('blogs_post'), data=data2, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response = self.user_client.post(path=reverse('blogs_post'), data=data3, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put(self):
        data_update = {
            "title": self.fake.text()[:19],
            "text": self.fake.text()
        }
        response = self.user_client.put(path=self.url_pk, data=data_update, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        response = self.user_client.delete(path=self.url_pk, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
