import urllib.parse
import re

def validate_url(raw: str) -> str:
    cleaned = raw.strip()
    if not cleaned:
        raise ValueError("URL cannot be empty.")
    if len(cleaned) > 2048:
        raise ValueError("URL exceeds maximum length of 2048 characters.")
    
    parsed = urllib.parse.urlparse(cleaned)
    if parsed.scheme not in ('http', 'https'):
        raise ValueError("Invalid scheme. Only HTTP and HTTPS are supported.")
    if not parsed.netloc:
        raise ValueError("Invalid URL: missing netloc.")
        
    return cleaned
