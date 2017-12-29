from django.contrib import admin

from .models import Route, RouteStatus, Driver


class RouteAdmin(admin.ModelAdmin):
    class Meta:
        model = Route


admin.site.register(Route, RouteAdmin)


class RouteStatusAdmin(admin.ModelAdmin):
    class Meta:
        model = RouteStatus


admin.site.register(RouteStatus, RouteStatusAdmin)


class DriverAdmin(admin.ModelAdmin):
    class Meta:
        model = Driver


admin.site.register(Driver, DriverAdmin)
