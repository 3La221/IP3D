from django import template

register = template.Library()

@register.filter(name='replace')
def replace(value, args):
    """
    Replace occurrences of a substring with another substring.
    Args should be a string in the format 'old,new'.
    Example usage: {{ value|replace:"old,new" }}
    """
    try:
        old_value, new_value = args.split('|', 1)
        return value.replace(old_value, new_value)
    except ValueError:
        # If the split fails, return the original value
        return value
