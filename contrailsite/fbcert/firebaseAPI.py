import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json
import requests

# Use a service account
cred = credentials.Certificate('contrailsite/fbcert/contrate-5064b-firebase-adminsdk-kraka-ae13d9defa.json')
firebase_admin.initialize_app(cred)

db = firestore.client()


def getCargoTypes(name=''):

    collection = db.collection(u'cargotype')

    if name != '':
        query = collection.where(u'name', u'==', name)
    else:
        query = collection.order_by('name')

    docs = query.stream()

    arr = []

    for doc in docs:
        arr.append(doc.to_dict())

    return arr


def getCountries(name='', id=''):

    collection = db.collection(u'countries')

    query = collection.order_by('name')

    if name != '':
        query = query.where(u'name', u'==', name)

    if id != '':
        query = query.where(u'id', u'==', id)

    docs = query.stream()

    arr = []

    for doc in docs:
        arr.append(doc.to_dict())

    return arr


def getPorts(name='', country='', id=''):

    collection = db.collection(u'ports')

    query = collection.order_by('name')

    if name != '':
        query = query.start_at([name]).end_at([name + '\uf8ff'])

    if id != '':
        query = query.where(u'id', u'==', id)

    if country != '':
        query = query.where(u'country.name', u'==', country)

    docs = query.stream()

    arr = []

    for doc in docs:
        arr.append(doc.to_dict())

    return arr


def getAirports(name=''):

    collection = db.collection(u'airports')

    query = collection.order_by('name').limit(3)

    if name != '':
        query = query.start_at([name]).end_at([name + '\uf8ff']).limit(3)

    docs = query.stream()

    arr = []

    for doc in docs:
        arr.append(doc.to_dict())

    return arr


def setAerodromsinfo():

    return
    with open('contrailsite/fbcert/data/russian_aerodroms.json', encoding='utf-8-sig') as f:

        id = '6007'
        flag = False
        templates = json.load(f)

        if 'features' in templates:
            print(len(templates['features']))
            for i in templates['features']:
                if id == i['properties']['addition']['id'] or id == '' and flag is not True:
                    flag = True
                    print('пропустили:', i['properties']['addition']['id'])
                    continue

                if flag:

                    # print(i)

                    result = requests.get("https://fpln.ru/api/info/AD/" + i['properties']['addition']['id'])
                    txt = result.text

                    data = json.loads(txt)

                    if 'id' in data:
                        doc_ref = db.collection(u'airports').document(data['id'])
                        doc_ref.set(data)
                        print("загрузили", data['id'])


def setData():

    return
    with open('contrailsite/fbcert/data/ports.json', encoding='utf-8') as f:
        templates = json.load(f)
        point = 0
        flag = False
        for i in templates['countries']:

            for x in i['ports']:

                point += 1

                name = x['name'].replace('/', " ")

                if x['name'] == 'Neustadt/Holstein':
                    flag = True

                if flag:

                    doc_ref = db.collection(u'ports').document(name)

                    x['country'] = {
                        u'name': i['name'],
                        u'url': i['url'],
                        u'icon': i['icon']
                    }

                    if "port_det" in x['data']:
                        long_arr = x['data']['port_det']['_Долгота_colon_'].split()
                        lat_arr = x['data']['port_det']['_Широта_colon_'].split()

                        long = int(long_arr[0].replace('º', '')) + int(long_arr[1].replace('\'', '')) / 60 + int(long_arr[2].replace('\'\'', '')) / 3600
                        lat = int(lat_arr[0].replace('º', '')) + int(lat_arr[1].replace('\'', '')) / 60 + int(lat_arr[2].replace('\'\'', '')) / 3600
                    else:
                        long = 0
                        lat = 0

                    x['longitude'] = long
                    x['latitude'] = lat
                    print(point, x['name'], lat, long)

                    doc_ref.set(x)


class Country:

    def __init__(self, id):

        self.id = id
        self.getObject()

    def getObject(self):

        data = getCountries(name=self.id)

        if len(data) > 0:

            for i in data[0].keys():
                setattr(self, i, data[0][i])

        print(self.__dict__)


class Port:

    def __init__(self, id):

        self.id = id
        self.getObject()

    def getObject(self):

        data = getPorts(id=self.id)

        setattr(self, 'name', data[0]['name'])
        setattr(self, 'id', data[0]['id'])
        setattr(self, 'country', Country(data[0]['country']['name']))


class Container:

    def __init__(self, id):

        self.id = id
        self.getObject()

    def getObject(self):

        data = getCargoTypes(name=self.id)

        setattr(self, 'name', data[0]['name'])
        setattr(self, 'iso', data[0]['iso'])

# getCountries()
