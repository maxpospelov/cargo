from django import forms
from .models import Route


class CreateRouteForm(forms.ModelForm):
    class Meta(object):
        model = Route
        fields = ['route', 'driver', 'phone']

    driver = forms.CharField(label='Driver', max_length=100)
    phone = forms.CharField(label='Phone', max_length=100)
    route = forms.CharField(label='Route', max_length=100)


class EditRouteForm(forms.ModelForm):
    class Meta(object):
        model = Route
        fields = ['route', 'driver', 'phone']

    driver = forms.CharField(label='Driver', max_length=100)
    phone = forms.CharField(label='Phone', max_length=100)
    route = forms.CharField(label='Route', max_length=100)
