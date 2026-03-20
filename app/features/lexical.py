import re

def extract_lexical(url: str) -> dict:
    suspicious_keywords = ['login', 'verify', 'secure', 'account', 'update', 'banking', 'confirm', 'signin', 'password']
    
    url_length = len(url)
    digit_count = len(re.findall(r'\d', url))
    hyphen_count = url.count('-')
    dot_count = url.count('.')
    has_at_symbol = 1 if '@' in url else 0
    has_double_slash = 1 if '//' in url[7:] else 0
    
    url_lower = url.lower()
    suspicious_keyword_count = sum(1 for kw in suspicious_keywords if kw in url_lower)
    
    return {
        'url_length': url_length,
        'digit_count': digit_count,
        'hyphen_count': hyphen_count,
        'dot_count': dot_count,
        'has_at_symbol': has_at_symbol,
        'has_double_slash': has_double_slash,
        'suspicious_keyword_count': suspicious_keyword_count
    }
