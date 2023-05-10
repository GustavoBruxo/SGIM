from django import template

register = template.Library()


def replace(value):
    return str(value).replace(',','.')


register.filter('replace', replace)
