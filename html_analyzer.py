from html.parser import HTMLParser

class LinkExtractor(HTMLParser):
    """Extract hyperlinks and their displayed text from HTML."""

    def __init__(self):
        super().__init__()
        self.links = []
        self.current_link = None

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            attributes = dict(attrs)

            href = attributes.get("href")

            if href:
                self.current_link = {
                    "url": href,
                    "text": ""
                }
    
    def handle_data(self, data):

        if self.current_link is not None:
            self.current_link["text"] += data.strip()

    def handle_endtag(self, tag):

        if tag == "a" and self.current_link is not None:
            self.links.append(self.current_link)
            self.current_link = None

def extract_links(html_content):
    """Extract hyperlinks from HTML content."""

    parser = LinkExtractor()
    parser.feed(html_content)

    return parser.links

if __name__ == "__main__":

    sample_html = """
    <html>
    <body>
        <a href="https://attacker.example/login">
            https://company.example
        </a>

        <a hred="https://google.com">
            Google
        </a>

    </body>
    </html>
    """

    results = extract_links(sample_html)

    for link in results:
        print("Displayed text:", link["text"])
        print("Actual URL:", link["url"])
        print("-" * 40)