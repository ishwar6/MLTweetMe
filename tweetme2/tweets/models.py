from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Tweet(models.Model):
    TYPES = (
        ('U', "User"),
        ("A", "Administrator")
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # models.SET_NULL
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to="", blank=True)
    user_type = models.CharField(choices=TYPES, max_length=1)


class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)
