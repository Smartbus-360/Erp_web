from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """
    Usage: {{ my_dict|get_item:my_key }}
    """
    if not dictionary:
        return ""
    return dictionary.get(key, "")
