from app.features.extractor import extract_features, FEATURE_NAMES

def test_extract_features():
    url = 'http://login-verify.suspicious.com/account?id=1'
    features = extract_features(url)
    
    assert len(features) == 12
    uses_https_idx = FEATURE_NAMES.index('uses_https')
    assert features[uses_https_idx] == 0
    
    suspicious_idx = FEATURE_NAMES.index('suspicious_keyword_count')
    assert features[suspicious_idx] >= 2
    
    query_idx = FEATURE_NAMES.index('query_param_count')
    assert features[query_idx] == 1
