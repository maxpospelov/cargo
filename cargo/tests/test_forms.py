from django.test import TestCase
from django.test.client import RequestFactory

from ..forms import CreateRouteForm, EditRouteForm


class CreateRouteFormTestCase(TestCase):

    def setUp(self):
        self.data = {
            "driver": "John",
            "phone": "895098712378",
            "route": "EKB"
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
        self.data = {
            "driver": "John",
            "phone": "895098712378",
            "route": "EKB"
        }

        self.request = RequestFactory().get("/route/1/edit")

    def test_fields_needed(self):
        form = EditRouteForm(self.data)
        self.assertTrue(form.is_valid())

    def test_required_field(self):
        self.data["route"] = None
        form = EditRouteForm(self.data)
        self.assertFalse(form.is_valid())
