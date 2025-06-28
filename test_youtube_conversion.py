"""
Test script for YouTube URL conversion
Run this to test the YouTube URL conversion functionality
"""

def test_youtube_conversion():
    # Sample YouTube URLs in different formats
    test_urls = [
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "https://youtu.be/dQw4w9WgXcQ",
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=30s",
        "https://youtu.be/dQw4w9WgXcQ?t=30",
        "https://www.youtube.com/embed/dQw4w9WgXcQ",
    ]
    
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

    def youtube_embed_url(value):
        """Convert any YouTube URL to embed format with optimal parameters."""
        video_id = youtube_video_id(value)
        if video_id:
            return f"https://www.youtube.com/embed/{video_id}?autoplay=0&mute=0&controls=1&rel=0"
        return value if value else ""
    
    print("YouTube URL Conversion Test")
    print("=" * 50)
    
    for url in test_urls:
        video_id = youtube_video_id(url)
        embed_url = youtube_embed_url(url)
        print(f"Original: {url}")
        print(f"Video ID: {video_id}")
        print(f"Embed URL: {embed_url}")
        print("-" * 50)

if __name__ == "__main__":
    test_youtube_conversion()
