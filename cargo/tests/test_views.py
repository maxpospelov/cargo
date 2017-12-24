from django.test import TestCase


from cargo.models import Route


try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse


class RouteListViewTest(TestCase):
    def setUp(self):
        Route.objects.create(driver='Driver A', phone='89509871234', route='Kazan')
        Route.objects.create(driver='Driver B', phone='89509871235', route='Kazan')

    def test_context(self):
        response = self.client.get(
            reverse("route_list")
        )

        self.assertEquals(response.context_data["route_list"].count(), 2)
        self.assertEquals(response.context_data["route_list"][0].phone, '89509871234')


class RouteCreateViewTest(TestCase):
    def test_post(self):
        response = self.client.post(
            reverse("route_create"),
            {'phone': '89509871234', 'route': 'EKB', 'driver': 'Driver A'}
        )

        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, reverse("route_list"))

    def test_post_on_error(self):
        response = self.client.post(
            reverse("route_create"),
            {}
        )

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context_data["form"].is_valid(), False)


class RouteUpdateViewTest(TestCase):
    def test_post(self):
        Route.objects.create(id=1, driver='Driver A', phone='89509871234', route='Kazan')

        response = self.client.post(
            reverse("route_update", args=[1]),
            {'id': 1, 'phone': '89509871234', 'route': 'EKB', 'driver': 'Driver A'}
        )

        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, reverse("route_list"))

        route = Route.objects.get(id=1)

        self.assertEquals(route.route, 'EKB')


class RouteDeleteViewTest(TestCase):
    def test_post(self):
        Route.objects.create(id=1, driver='Driver A', phone='89509871234', route='Kazan')

        response = self.client.post(
            reverse("route_delete", args=[1]),
            {}
        )

        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, reverse("route_list"))

        route = Route.objects.all()

        self.assertEquals(len(route), 0)


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

    def test_not_save_empty_driver(self):
        self.client.get('/')
        self.assertEqual(Route.objects.count(), 0)

    def test_dispaly_all_route(self):
        Route.objects.create(driver='Driver A')
        Route.objects.create(driver='Driver B')

        response = self.client.get('/')

        self.assertIn('Driver A', response.content.decode())
        self.assertIn('Driver B', response.content.decode())