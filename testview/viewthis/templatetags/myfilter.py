from django import template

register = template.Library()

@register.filter
def myreplace(value):
	return value.lower()