import warnings
from django import template

register = template.Library()

@register.filter(is_safe=False)
def replace(value, args):
    """Replace occurrences of old_value with new_value in the given string."""
    try:
        old_value, new_value = args.split('|', 1)
        return value.replace(old_value, new_value)
    except ValueError:
        # If the split fails, return the original value
        return value

@register.filter(is_safe=False)
def length_is(value, arg):
    """Return a boolean of whether the value's length is the argument."""
    warnings.warn(
        "The length_is template filter is deprecated in favor of the length template "
        "filter and the == operator within an {% if %} tag.",
        DeprecationWarning,  # Use DeprecationWarning instead of RemovedInDjango51Warning
    )
    try:
        return len(value) == int(arg)
    except (ValueError, TypeError):
        return ""