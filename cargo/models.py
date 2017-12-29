from django.db import models


class RouteStatus(models.Model):
    status = models.CharField(max_length=20)

    def __str__(self):
        return '{}'.format(self.status)


class Driver(models.Model):
    name = models.TextField(default='')
    phone = models.TextField(default='')

    def __str__(self):
        return '{}({})'.format(self.name, self.phone)


class Route(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True)
    status = models.ForeignKey(RouteStatus, on_delete=models.CASCADE, null=True)
    route = models.TextField(default='')
    gate = models.TextField(null=True)
