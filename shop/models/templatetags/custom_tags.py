from django import template

register = template.Library()

@register.filter(name='multiply')

def multiply(q , p ):
    return p*q