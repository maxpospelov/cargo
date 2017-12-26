from django import forms
from .models import Route, RouteStatus


class CreateRouteForm(forms.ModelForm):
    class Meta(object):
        model = Route
        fields = ['route', 'driver', 'phone', 'status', 'gate']

    driver = forms.CharField(label='Driver', max_length=100)
    phone = forms.CharField(label='Phone', max_length=100)
    route = forms.CharField(label='Route', max_length=100)
    gate = forms.CharField(label='Gate', max_length=100)
    status = forms.ModelChoiceField(queryset=RouteStatus.objects.all())


class EditRouteForm(forms.ModelForm):
    class Meta(object):
        model = Route
        fields = ['route', 'driver', 'phone', 'status', 'gate']

    driver = forms.CharField(label='Driver', max_length=100)
    phone = forms.CharField(label='Phone', max_length=100)
    route = forms.CharField(label='Route', max_length=100)
    gate = forms.CharField(label='Gate', max_length=100)
    status = forms.ModelChoiceField(queryset=RouteStatus.objects.all())
