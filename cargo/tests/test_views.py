from django.test import TestCase
from django.contrib.auth import get_user_model

from cargo.models import Route, RouteStatus, Driver


try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse


class RouteListViewTest(TestCase):
    def setUp(self):
        driver1 = Driver.objects.create(id=2, name='Driver A', phone='89509871234')
        driver2 = Driver.objects.create(id=3, name='Driver B', phone='89509871235')

        Route.objects.create(driver=driver1, route='Kazan', gate="8")
        Route.objects.create(driver=driver2, route='Kazan')

    def test_context(self):
        response = self.client.get(
            reverse("route_list")
        )

        self.assertEquals(response.context_data["route_list"].count(), 2)
        self.assertEquals(response.context_data["route_list"][0].driver.phone, '89509871234')
        self.assertEquals(response.context_data["route_list"][0].driver.name, 'Driver A')
        self.assertEquals(response.context_data["route_list"][1].driver.phone, '89509871235')
        self.assertEquals(response.context_data["route_list"][1].driver.name, 'Driver B')
        self.assertEquals(response.context_data["route_list"][0].gate, '8')
        self.assertEquals(response.context_data["route_list"][1].gate, None)


class RouteCreateViewTest(TestCase):
    def setUp(self):
        self.driver = Driver.objects.create(id=2, name='Driver A', phone='89509871234')
        self.status = RouteStatus.objects.create(id=1, status='load')

    def test_post(self):
        response = self.client.post(
            reverse("route_create"),
            {
                'route': 'EKB',
                'driver': 2,
                'status': 1,
                'gate': '9'}
        )

        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, reverse("route_list"))

    def test_post_on_error(self):
        response = self.client.post(
            reverse("route_create"),
            {
                'route': None,
                'driver': None,
                'status': 1,
                'gate': '9'}
        )

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context_data["form"].is_valid(), False)


class RouteUpdateViewTest(TestCase):
    def setUp(self):
        self.driver = Driver.objects.create(id=2, name='Driver A', phone='89509871234')
        self.status = RouteStatus.objects.create(id=1, status='load')

    def test_post(self):
        Route.objects.create(id=1, driver=self.driver, route='Kazan')

        response = self.client.post(
            reverse("route_update", args=[1]),
            {
                'id': 1,
                'route': 'EKB',
                'driver': 2,
                'status': 1,
                'gate': '8'}
        )

        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, reverse("route_list"))

        route = Route.objects.get(id=1)

        self.assertEquals(route.route, 'EKB')


class RouteDeleteViewTest(TestCase):
    def test_post(self):
        driver = Driver.objects.create(id=2, name='Driver A', phone='89509871234')
        Route.objects.create(id=1, driver=driver, route='Kazan')

        response = self.client.post(
            reverse("route_delete", args=[1]),
            {}
        )

        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, reverse("route_list"))

        route = Route.objects.all()

        self.assertEquals(len(route), 0)


class DriverUpdateViewTest(TestCase):
    def test_post(self):
        Driver.objects.create(id=1, name='Driver A', phone='911')

        response = self.client.post(
            reverse("driver_update", args=[1]),
            {
                'id': 1,
                'name': 'Driver B',
                'phone': '922'}
        )

        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, reverse("route_list"))

        driver = Driver.objects.get(id=1)

        self.assertEquals(driver.name, 'Driver B')


class DriverCreateViewTest(TestCase):
    def test_post(self):
        response = self.client.post(
            reverse("driver_create"),
            {
                'name': 'Driver A',
                'phone': '89506431289'}
        )

        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, reverse("route_create"))

    def test_post_on_error(self):
        response = self.client.post(
            reverse("driver_create"),
            {}
        )

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context_data["form"].is_valid(), False)
        self.assertIn('This field is required', response.content.decode())


class HomePageTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="luke",
            email="luke@example.com",
            password="password"
        )

        self.client.login(username='luke', password='password')

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_dispaly_all_route(self):
        Driver.objects.create(id=2, name='Driver A', phone='89509871234')
        Driver.objects.create(id=3, name='Driver B', phone='89509871233')

        drivers = Driver.objects.all()

        RouteStatus.objects.create(id=1, status='load')
        status = RouteStatus.objects.all()

        Route.objects.create(id=1, route='A', driver=drivers[0], status=status[0])
        Route.objects.create(id=2, route='B', driver=drivers[1], status=status[0])

        routes = Route.objects.all()
        self.assertEqual(routes.count(), 2)

        response = self.client.get('/')

        self.assertIn('Driver A', response.content.decode())
        self.assertIn('Driver B', response.content.decode())