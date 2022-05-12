from django.db import models
from django.contrib.auth.models import User
import uuid
import datetime
import json


class CargoType(models.Model):
    # 7.5,8.5,11,27,31,32,33,135,145,155,165,175,185,195,205,215,225,235,245,255,265,275,285,295,305,315,325,335,355
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID")
    name = models.CharField(max_length=100, default="")
    iso = models.CharField(max_length=100, default="")

    def __str__(self):
        return str(self.name)

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
