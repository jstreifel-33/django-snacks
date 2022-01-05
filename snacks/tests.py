from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.

class SnacksTestCase(SimpleTestCase):
    def _get_url(self, name):
        url = reverse(name)
        response = self.client.get(url)
        return response

    def test_home_status_code(self):
        res = self._get_url('home')
        self.assertEqual(res.status_code, 200)
    
    def test_home_template(self):
        res = self._get_url('home')
        self.assertTemplateUsed(res, 'home.html')
        self.assertTemplateUsed(res, '_base.html')

    def test_about_status_code(self):
        res = self._get_url('about')
        self.assertEqual(res.status_code, 200)

    def test_about_template(self):
        res = self._get_url('about')
        self.assertTemplateUsed(res, 'about.html')
        self.assertTemplateUsed(res, '_base.html')
        