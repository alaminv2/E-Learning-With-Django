from django import template

register = template.Library()


def range_article(value):
    return value[0:150] + '..............'


register.filter('range_article', range_article)
