from django import template

register = template.Library()

@register.filter
def mediapath(image_path):
    return image_path.url
