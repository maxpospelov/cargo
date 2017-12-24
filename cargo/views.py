from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from cargo.models import Route


class RouteListView(ListView):
    model = Route
    context_object_name = 'route_list'
    template_name = 'route_list.html'

    def get_queryset(self):
        return super(RouteListView, self).get_queryset()


class RouteCreateView(CreateView):
    model = Route
    fields = ['route', 'driver', 'phone']
    template_name = 'route_create.html'
    success_url = '/routes/'


class RouteEditView(UpdateView):
    model = Route
    fields = ['route', 'driver', 'phone']
    template_name = 'route_edit.html'
    success_url = '/routes/'


class RouteDeleteView(DeleteView):
    model = Route
    template_name = 'route_delete.html'
    success_url = '/routes/'


def home_page(request):
    if request.method == 'POST':
        Route.objects.create(driver=request.POST['driver'])
        return redirect('/')

    routes = Route.objects.all()
    return render(request, 'home.html', {'routes': routes})
