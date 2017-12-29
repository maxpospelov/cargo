from cargo.models import Route, RouteStatus, Driver
from django.test import TestCase


class TestRoute(TestCase):
    def test_saving_driver(self):
        first_status = RouteStatus()
        first_status.status = 'Load'

        first_status.save()

        driver = Driver()
        driver.name = 'Driver A'
        driver.phone = '89506783541'
        driver.save()

        first_driver = Route()

        first_driver.driver = driver
        first_driver.status = first_status

        first_driver.gate = '56'

        first_driver.save()

        saved_driver = Route.objects.all()

        self.assertEqual(saved_driver.count(), 1)
        self.assertEqual(saved_driver[0].driver.name, 'Driver A')
        self.assertEqual(saved_driver[0].driver.phone, '89506783541')
        self.assertEqual(saved_driver[0].status.status, 'Load')
        self.assertEqual(saved_driver[0].gate, '56')


class TestRouteStatus(TestCase):
    def test_saving_status(self):
        first_status = RouteStatus()
        first_status.status = 'Load'

        first_status.save()
        saved_status = RouteStatus.objects.all()

        self.assertEqual(saved_status.count(), 1)
        self.assertEqual(saved_status[0].status, 'Load')


class TestDriver(TestCase):
    def test_saving_driver(self):
        driver = Driver()
        driver.name = 'John'
        driver.phone = '8976123456'

        driver.save()
        drivers = Driver.objects.all()

        self.assertEqual(drivers.count(), 1)
        self.assertEqual(drivers[0].name, 'John')
        self.assertEqual(drivers[0].phone, '8976123456')
