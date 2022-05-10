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
    path('referencebook/countries/', views.countries, name='countries'),
    path('referencebook/countriesmap/', views.countriesmap, name='countries'),
    path('referencebook/containers/', views.containers, name='containers'),
    path('referencebook/ports/', views.ports, name='ports'),
    # path('accounts/registration/', views.registration, name='registration'),

]
