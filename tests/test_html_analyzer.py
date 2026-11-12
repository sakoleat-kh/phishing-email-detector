from html_analyzer import extract_links

def test_extract_single_link():
    html = '<a href="https://example.com">Example</a>'

    result = extract_links(html)

    assert len(result) == 1
    assert result[0]["url"] == "https://example.com"
    assert result[0]["text"] == "Example"

def test_extract_multiple_links():
    html = """
    <a href="https://google.com">Google</a>
    <a href="https://github.com">GitHub</a>
    """

    result = extract_links(html)

    assert len(result) == 2

def test_extract_mismatched_displayed_url():
    html = """
    <a href="https://attacker.example/login">
        https://company.example
    </a>
    """

    result = extract_links(html)

    assert result[0]["url"] == "https://attacker.example/login"
    assert result[0]["text"] == "https://company.example"

def test_html_without_links():
    html = "<html><body><p>Hello world</p></body></html>"

    result = extract_links(html)

    assert result == []