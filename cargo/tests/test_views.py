from django.test import TestCase

from cargo.models import Route


class HomePageTest(TestCase):
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'driver': 'Driver A'})

        self.assertEqual(Route.objects.count(), 1)
        new_driver = Route.objects.first()
        self.assertEqual(new_driver.driver, 'Driver A')

    def test_redirects_after_POST(self):
        response = self.client.post('/', data={'driver': 'Driver A'})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_not_save_empty_driver(self):
        self.client.get('/')
        self.assertEqual(Route.objects.count(), 0)

    def test_dispaly_all_route(self):
        Route.objects.create(driver='Driver A')
        Route.objects.create(driver='Driver B')

        response = self.client.get('/')

        self.assertIn('Driver A', response.content.decode())
        self.assertIn('Driver B', response.content.decode())