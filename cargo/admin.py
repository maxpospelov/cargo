from django.contrib import admin

# Register your models here.
from .models import Route


class RouteAdmin(admin.ModelAdmin):
    class Meta:
        model = Route


admin.site.register(Route, RouteAdmin)
