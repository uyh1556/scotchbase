# whisky/templatetags/whisky_extras.py
from django import template

register = template.Library()

@register.filter
def remove_last_part(value, delimiter=','):
    parts = value.rsplit(delimiter, 1)
    return parts[0] if len(parts) > 1 else value

