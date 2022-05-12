from django.shortcuts import render
from django.http import HttpResponse
import contrailsite.fbcert.firebaseAPI as firebaseAPI
# Create your views here.


def robots(request):
    lines = [
        "User-Agent: *",
        "Host: https://xn----otbpfaehjj6c9a.xn--p1ai",
        "Sitemap: https://xn----otbpfaehjj6c9a.xn--p1ai/sitemap.xml",
        "Disallow: /admin/",
        "Disallow: /auth/",
        "Disallow: /lk/",
        "Disallow: /cart/",
        "Disallow: /accounts/",
        "Disallow: /api/",
        "Disallow: /profile/",
        "User-Agent: Googlebot-Image",
        "Allow: /media/",
        "Allow: /static/img",
        "User-Agent: YandexImages",
        "Allow: /media/",
        "Allow: /static/img"
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")


def test(request):
    return HttpResponse("Hello, world. You're at the test page.")


def index(request):

    return render(
        request,
        'tmplts/main.html',
        context={"data": countries}
    )


# Справочники

def countries(request):

    data = firebaseAPI.getCountries('')

    arr_th = []

    if len(data) != 0:
        for i in data[0].keys():
            arr_th.append(i)

    return render(
        request,
        'tmplts/datatable.html',
        context={"data": data, "h3": "Страны мира", "headers": arr_th}
    )


def countriesmap(request):

    countries = firebaseAPI.getCountries('')

    return render(
        request,
        'tmplts/countriesmap.html',
        context={"data": countries}
    )


def containers(request):

    data = firebaseAPI.getCargoTypes('')
    arr_th = []

    if len(data) != 0:
        for i in data[0].keys():
            arr_th.append(i)

    return render(
        request,
        'tmplts/datatable.html',
        context={"data": data, "h3": "Контейнеры", "headers": arr_th}
    )


def ports(request):

    country = request.GET.get("country", 'H&*78fegt834pgth3p')
    countries = firebaseAPI.getPorts(country=country)

    for i in countries:
        print(i['name'], i['latitude'], i['longitude'])

    return render(
        request,
        'tmplts/portsmap.html',
        context={"data": countries}
    )


def airports(request):

    data = firebaseAPI.getAirports('')
    arr_th = []

    if len(data) != 0:
        for i in data[0].keys():
            arr_th.append(i)

    return render(
        request,
        'tmplts/datatable.html',
        context={"data": data, "h3": "Аэропорты", "headers": arr_th}
    )


# Формы

def port(request):

    id = request.GET.get("id", 'H&*78fegt834pgth3p')

    print(id)

    port = firebaseAPI.Port(id)

    return render(
        request,
        'tmplts/dataform.html',
        context={"data": port.__dict__, "h3": "Порт: " + port.name}
    )


def container(request):

    id = request.GET.get("id", 'H&*78fegt834pgth3p')

    print(id)

    data = firebaseAPI.Container(id)

    return render(
        request,
        'tmplts/dataform.html',
        context={"data": data.__dict__, "h3": "Контейнер: " + data.name}
    )
