from django.db import models


class RouteStatus(models.Model):
    status = models.CharField(max_length=20)

    def __str__(self):
        return '{}'.format(self.status)


class Route(models.Model):
    driver = models.TextField(default='')
    phone = models.TextField(default='')
    route = models.TextField(default='')
    status = models.ForeignKey(RouteStatus, on_delete=models.CASCADE, null=True)
