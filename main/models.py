from django.db import models
from django.contrib.auth.models import User
import uuid
import datetime
import json


class CargoType(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID")
    name = models.CharField(max_length=100, default="")
    iso = models.CharField(max_length=100, default="")

    def __str__(self):
        return str(self.name)

    def get_heading():
        return "name,id,iso"

    def get_all(fields=""):

        if fields == "":
            fields = CargoType.get_heading()

        data = []
        query = CargoType.objects.all()

        for i in query:
            el = {}
            for y in fields.split(','):
                el[y] = i.__dict__[y]

            el['url'] = "/referencebook/cargoType?id=" + str(i.__dict__['id'])

            data.append(el)

        return data

    def get_by_name(name):

        if name == "":
            return CargoType.objects.get(id="00000000-0000-0000-0000-000000000000")

        try:
            elem = CargoType.objects.get(name=name)
        except Exception:
            elem = CargoType()
            elem.name = name
            elem.save()

        return elem


class TransportUnit(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID")
    name = models.CharField(max_length=100, default="")
    cargoType = models.ForeignKey('CargoType', on_delete=models.CASCADE, blank=True, default="00000000-0000-0000-0000-000000000000")

    def __str__(self):
        return str(self.name)

    def get_by_name(name):

        if name == "":
            return TransportUnit.objects.get(id="00000000-0000-0000-0000-000000000000")

        try:
            elem = TransportUnit.objects.get(name=name)
        except Exception:
            elem = TransportUnit()
            elem.name = name
            elem.save()

        return elem
