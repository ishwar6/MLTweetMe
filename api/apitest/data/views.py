from django.shortcuts import render
from data.models import Person
from rest_framework import viewsets
from .serilizer import PersonSerializer


class PersonView(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
