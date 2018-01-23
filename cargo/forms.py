from django import forms
from .models import Route, RouteStatus, Driver


class CreateRouteForm(forms.ModelForm):
    class Meta(object):
        model = Route
        fields = ['route', 'driver', 'status', 'gate']

    driver = forms.ModelChoiceField(queryset=Driver.objects.all())
    route = forms.CharField(label='Route', max_length=100)
    gate = forms.CharField(label='Gate', max_length=100, required=False)
    status = forms.ModelChoiceField(queryset=RouteStatus.objects.all())


class EditRouteForm(forms.ModelForm):
    class Meta(object):
        model = Route
        fields = ['route', 'driver', 'status', 'gate']

    driver = forms.ModelChoiceField(queryset=Driver.objects.all())
    route = forms.CharField(label='Route', max_length=100)
    gate = forms.CharField(label='Gate', max_length=100, required=False)
    status = forms.ModelChoiceField(queryset=RouteStatus.objects.all())


class DriverCreateForm(forms.ModelForm):
    class Meta(object):
        model = Driver
        fields = ['name', 'phone']

    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=100)


class DriverEditForm(forms.ModelForm):
    class Meta(object):
        model = Driver
        fields = ['name', 'phone']

    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=100)
