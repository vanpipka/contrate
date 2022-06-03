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

    def get_url():
        return "http://127.0.0.1:555/api/cargoTypes/"

    def get_heading():
        return {"id": "Идентификатор", "name": "Наименование", "iso": "ISO"}

    def get_all(fields="", params={}):

        if fields == "":
            fields = CargoType.get_heading()

        query = CargoType.objects.all()

        return get_data_on_params(query, fields.keys(), params)

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

    def get_url():
        return "http://127.0.0.1:555/api/transportUnits/"

    def get_heading():
        return {"id": "Идентификатор", "name": "Наименование", "cargoType": "Тип"}

    def get_all(fields="", params={}):

        if fields == "":
            fields = TransportUnit.get_heading()

        query = TransportUnit.objects.select_related('cargoType').all()

        return get_data_on_params(query, fields.keys(), params)

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

# ADDITIONAL

def get_data_on_params(query, fields, params):

    print(params)

    result = {"totalNotFiltered": len(query)}

    # params
    sort = params.get("sort", "")
    search = params.get("search", "")
    order = params.get("order", "")
    offset = int(params.get("offset", "0"))
    limit = offset + int(params.get("limit","0"))

    if sort !="" and order !="" :
        if order == 'asc':
            query = query.order_by('-'+params['sort'])
        else:
            query = query.order_by(params['sort'])

    data = []

    for i in query:
        el = {}
        need_to_add = False
        for y in fields:

            if y == 'cargoType':
                el[y] = i.cargoType.name
            else:
                el[y] = i.__dict__[y]

            if search != "":
                if search in str(el[y]):
                    need_to_add = True
            else:
                need_to_add = True

        if need_to_add:

            el['url'] = "/referencebook/transportUnit?id=" + str(i.__dict__['id'])

            data.append(el)

    result['rows'] = data[offset:limit]
    result['total'] = len(data)

    print(offset,limit)

    return result
