from django.db import models


class Route(models.Model):
    driver = models.TextField(default='')
    phone = models.TextField(default='')
    route = models.TextField(default='')