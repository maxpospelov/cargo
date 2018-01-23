from django.test import TestCase
from django.test.client import RequestFactory

from ..forms import CreateRouteForm, EditRouteForm, DriverEditForm
from ..models import RouteStatus, Driver, Route


class CreateRouteFormTestCase(TestCase):

    def setUp(self):
        RouteStatus.objects.create(id=1, status='load')
        self.status = RouteStatus.objects.all()

        Driver.objects.create(id=2, name='John', phone='895098712378')
        self.driver = Driver.objects.all()

        self.data = {
            "driver": self.driver,
            "route": "EKB",
            "status": self.status,
            "gate": "56"
        }

        self.request = RequestFactory().get("/route/create")

    def test_fields_needed(self):
        form = CreateRouteForm(self.data)
        self.assertTrue(form.is_valid())

    def test_required_field(self):
        self.data["route"] = None
        form = CreateRouteForm(self.data)
        self.assertFalse(form.is_valid())


class EditRouteFormTestCase(TestCase):

    def setUp(self):
        self.status = RouteStatus.objects.create(id=1, status='load')
        self.driver = Driver.objects.create(id=2, name='Driver A', phone='89509871234')

        Route.objects.create(id=1, driver=self.driver, status=self.status, route='Kazan', gate="8")

        self.data = {
            "driver": 2,
            "route": "EKB",
            "status": 1,
            "gate": "56"
        }

        self.request = RequestFactory().get("/route/1/edit")

    def test_fields_needed(self):
        form = EditRouteForm(self.data)
        self.assertTrue(form.is_valid())

    def test_required_field(self):
        self.data["route"] = None
        form = EditRouteForm(self.data)
        self.assertFalse(form.is_valid())


class EditDriverFormTestCase(TestCase):

    def setUp(self):
        self.driver = Driver.objects.create(id=2, name='Driver A', phone='89509871234')

        self.data = {
            "name": "Driver D",
            "phone": "89509871234"
        }

        self.request = RequestFactory().get("/driver/2/edit")

    def test_fields_requiered(self):
        form = DriverEditForm(self.data)
        self.assertTrue(form.is_valid())
