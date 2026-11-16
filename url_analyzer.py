
from urllib.parse import urlparse


def extract_hostname(url):
    """Extract and normalize the hostname from a URL."""

    if not url:
        return None

    parsed = urlparse(url.strip())

    if parsed.scheme.lower() not in ("http", "https"):
        return None

    if not parsed.hostname:
        return None

    return parsed.hostname.lower()

def compare_hostnames(visible_url, actual_url):
    """Compare hostnames from visible and actual URLs."""

    visible_hostname = extract_hostname(visible_url)
    actual_hostname = extract_hostname(actual_url)

    if not visible_hostname or not actual_hostname:
        return None
    
    return visible_hostname == actual_hostname


if __name__ == "__main__":

    test_urls = [
        "https://GOOGLE.COM/login",
        "HTTPS://Example.COM:8080/reset",
        "https://attacker.example/login",
        "Reset password"
    ]

    for url in test_urls:
        hostname = extract_hostname(url)

        print("Input:", url)
        print("Hostname:", hostname)
        print("-" * 40)

    print(compare_hostnames(
        "https://GOOGLE.COM/login",
        "https://google.com/reset"
    ))

    print(compare_hostnames(
        "https://company.example",
        "https://attacker.example/login"
    ))

    print(compare_hostnames(
        "Reset password",
        "https://attacker.example/login"
    ))
