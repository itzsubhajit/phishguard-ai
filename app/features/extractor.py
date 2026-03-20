from app.features.lexical import extract_lexical
from app.features.structural import extract_structural

FEATURE_NAMES = [
    'url_length', 'digit_count', 'hyphen_count', 'dot_count',
    'has_at_symbol', 'has_double_slash', 'suspicious_keyword_count',
    'uses_https', 'subdomain_depth', 'tld_in_path', 'path_depth', 'query_param_count'
]

def extract_features(url: str) -> list:
    lexical = extract_lexical(url)
    structural = extract_structural(url)
    combined = {**lexical, **structural}
    return [combined[key] for key in FEATURE_NAMES]
