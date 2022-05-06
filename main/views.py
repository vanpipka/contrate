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


def countries(request):

    countries = firebaseAPI.getCountries('')

    return render(
        request,
        'countries.html',
        context={"data": countries}
    )


def ports(request):

    country = request.GET.get("country", 'H&*78fegt834pgth3p')
    countries = firebaseAPI.getPorts(country=country)

    return render(
        request,
        'ports.html',
        context={"data": countries}
    )
