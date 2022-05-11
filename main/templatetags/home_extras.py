from django import template
from django.conf import settings
register = template.Library()


# Регистрируем тег, с помощью которого будем получать атрибуты из файла settings
@register.simple_tag
def get_attribute(name):
    return getattr(settings, name, "")


@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()


@register.filter(name='get_item')
def get_item(dictionary, key):
    return dictionary.get(key)
