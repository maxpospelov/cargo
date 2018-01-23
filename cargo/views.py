from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Route, Driver
from .forms import CreateRouteForm, EditRouteForm, DriverCreateForm, DriverEditForm
from django.contrib.auth.decorators import login_required


class RouteListView(ListView):
    model = Route
    context_object_name = 'route_list'
    template_name = 'route_list.html'

    def get_queryset(self):
        return super(RouteListView, self).get_queryset()


class RouteCreateView(CreateView):
    template_name = 'route_create.html'
    form_class = CreateRouteForm
    success_url = '/routes/'


class RouteEditView(UpdateView):
    model = Route
    form_class = EditRouteForm
    template_name = 'route_edit.html'
    success_url = '/routes/'


class RouteDeleteView(DeleteView):
    model = Route
    template_name = 'route_delete.html'
    success_url = '/routes/'


class DriverCreateView(CreateView):
    model = Driver
    form_class = DriverCreateForm
    template_name = 'driver_create.html'

    def get_success_url(self):
        return '/route/create/'


class DriverEditView(UpdateView):
    model = Driver
    form_class = DriverEditForm
    template_name = 'driver_edit.html'
    success_url = '/routes/'


@login_required
def home_page(request):
    if request.method == 'POST':
        Route.objects.create(driver=request.POST['driver'])
        return redirect('/')

    routes = Route.objects.all()
    return render(request, 'home.html', {'routes': routes})
