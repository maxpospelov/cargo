from django.shortcuts import render, redirect
from cargo.models import Route


def home_page(request):
    if request.method == 'POST':
        Route.objects.create(driver=request.POST['driver'])
        return redirect('/')

    routes = Route.objects.all()
    return render(request, 'home.html', {'routes': routes})
