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

@register.filter(is_safe=False)
def safe_video_url(value):
    """Safely convert YouTube URL to embed URL."""
    if not value:
        return ""
    try:
        # Handle different YouTube URL formats
        if "youtube.com/watch?v=" in value:
            # Standard YouTube link: https://www.youtube.com/watch?v=VIDEO_ID
            video_id = value.split("watch?v=")[1].split("&")[0]
            return f"https://www.youtube.com/embed/{video_id}"
        elif "youtu.be/" in value:
            # Short YouTube link: https://youtu.be/VIDEO_ID
            video_id = value.split("youtu.be/")[1].split("?")[0]
            return f"https://www.youtube.com/embed/{video_id}"
        elif "youtube.com/embed/" in value:
            # Already embedded format
            return value
        else:
            # For other video platforms or if it's already an embed URL
            return value
    except (AttributeError, TypeError, IndexError):
        return ""

@register.filter(is_safe=False)
def safe_default(value, default):
    """Return default value if the given value is None or empty."""
    if value is None or value == "":
        return default
    return value

@register.filter(is_safe=False)
def youtube_video_id(value):
    """Extract YouTube video ID from various URL formats."""
    if not value:
        return ""
    try:
        if "youtube.com/watch?v=" in value:
            return value.split("watch?v=")[1].split("&")[0]
        elif "youtu.be/" in value:
            return value.split("youtu.be/")[1].split("?")[0]
        elif "youtube.com/embed/" in value:
            return value.split("embed/")[1].split("?")[0]
        return ""
    except (AttributeError, TypeError, IndexError):
        return ""

@register.filter(is_safe=False)
def youtube_embed_url(value):
    """Convert any YouTube URL to embed format with optimal parameters."""
    video_id = youtube_video_id(value)
    if video_id:
        return f"https://www.youtube.com/embed/{video_id}?autoplay=0&mute=0&controls=1&rel=0"
    return value if value else ""