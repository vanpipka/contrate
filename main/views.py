from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import contrailsite.fbcert.firebaseAPI as firebaseAPI
import firebase_admin
from firebase_admin import credentials, db
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


def countries(request):

    countries = firebaseAPI.getCountries('')

    return render(
        request,
        'countries.html',
        context={"data": countries}
    )


def countriesmap(request):

    countries = firebaseAPI.getCountries('')

    return render(
        request,
        'tmplts/countriesmap.html',
        context={"data": countries}
    )


def containers(request):

    # countries = firebaseAPI.getCountries('')

    return render(
        request,
        'countries.html',
        context={"data": countries}
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
