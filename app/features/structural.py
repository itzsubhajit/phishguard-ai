import urllib.parse

def extract_structural(url: str) -> dict:
    parsed = urllib.parse.urlparse(url)
    
    uses_https = 1 if parsed.scheme == 'https' else 0
    
    subdomain_depth = max(0, parsed.netloc.count('.') - 1)
    
    tlds = ['.com', '.net', '.org', '.info', '.biz']
    tld_in_path = 1 if any(tld in parsed.path.lower() for tld in tlds) else 0
    
    path_depth = parsed.path.count('/')
    
    query_param_count = len(urllib.parse.parse_qs(parsed.query))
    
    return {
        'uses_https': uses_https,
        'subdomain_depth': subdomain_depth,
        'tld_in_path': tld_in_path,
        'path_depth': path_depth,
        'query_param_count': query_param_count
    }
