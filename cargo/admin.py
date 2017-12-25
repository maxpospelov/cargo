from django.contrib import admin

# Register your models here.
from .models import Route, RouteStatus


class RouteAdmin(admin.ModelAdmin):
    class Meta:
        model = Route


admin.site.register(Route, RouteAdmin)


class RouteStatusAdmin(admin.ModelAdmin):
    class Meta:
        model = RouteStatus


admin.site.register(RouteStatus, RouteAdmin)
