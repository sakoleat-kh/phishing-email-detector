
from url_analyzer import extract_hostname, compare_hostnames


def test_extract_lowercase_hostname():
    assert extract_hostname("https://GOOGLE.COM/login") == "google.com"


def test_extract_hostname_with_port():
    assert extract_hostname("https://Example.COM:8080/reset") == "example.com"


def test_extract_normal_hostname():
    assert extract_hostname("https://attacker.example/login") == "attacker.example"


def test_non_url_text():
    assert extract_hostname("Reset password") is None


def test_matching_hostnames():
    result = compare_hostnames(
        "https://GOOGLE.COM/login",
        "https://google.com/reset"
    )
    assert result is True


def test_different_hostnames():
    result = compare_hostnames(
        "https://company.example",
        "https://attacker.example/login"
    )
    assert result is False


def test_visible_text_is_not_url():
    result = compare_hostnames(
        "Reset password",
        "https://attacker.example/login"
    )
    assert result is None
