import pytest
from app.validators.url_validator import validate_url

def test_validate_url_valid_https():
    url = "https://www.google.com"
    assert validate_url(url) == url

def test_validate_url_valid_http():
    url = "http://login.verify.com/account"
    assert validate_url(url) == url

def test_validate_url_empty():
    with pytest.raises(ValueError):
        validate_url("")

def test_validate_url_no_scheme():
    with pytest.raises(ValueError):
        validate_url("not-a-url")

def test_validate_url_wrong_scheme():
    with pytest.raises(ValueError):
        validate_url("ftp://files.example.com")

def test_validate_url_too_long():
    long_url = "https://" + "a" * 2042
    with pytest.raises(ValueError):
        validate_url(long_url)
