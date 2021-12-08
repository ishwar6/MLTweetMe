from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=20)
    birth_year = models.CharField(max_length=4)
