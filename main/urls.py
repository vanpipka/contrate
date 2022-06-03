from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib.sitemaps.views import sitemap
# from .sitemaps import ProductSitemap, ModelSitemap

from . import views

# sitemaps = {
#    'products': ProductSitemap,
#    'autos': ModelSitemap
# }

urlpatterns = [
    path('', views.index),
    path('robots.txt', views.robots),
    # path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('test/', views.test, name='test'),

    # СПИСКИ
    path('referencebook/cargoTypes/', views.cargoTypes, name='cargoTypes'),
    path('referencebook/transportUnits/', views.transportUnits, name='transportUnits'),

    path('referencebook/countries/', views.countries, name='countries'),
    path('referencebook/airports/', views.airports, name='airports'),
    path('referencebook/countriesmap/', views.countriesmap, name='countriesmap'),
    path('referencebook/ports/', views.ports, name='ports'),

    # ФОРМЫ
    path('referencebook/port/', views.port, name='port'),
    path('referencebook/transportUnit/', views.transportUnit, name='transportUnit'),
    path('referencebook/cargoType/', views.cargoType, name='cargoType'),

    #API
    path('api/transportUnits/', views.api_transportUnits, name='api_transportUnits'),
    path('api/cargoTypes/', views.api_cargoTypes, name='api_cargoTypes'),
]
