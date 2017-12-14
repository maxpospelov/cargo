from django.db import models


class Route(models.Model):
    driver = models.TextField(default='')