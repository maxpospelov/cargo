from cargo.models import Route
from django.test import TestCase


class TestRoute(TestCase):
    def test_saving_driver(self):
        first_driver = Route()
        first_driver.driver = 'Driver A'
        first_driver.save()

        saved_driver = Route.objects.all()
        self.assertEqual(saved_driver.count(), 1)
        self.assertEqual(saved_driver[0].driver, 'Driver A')
