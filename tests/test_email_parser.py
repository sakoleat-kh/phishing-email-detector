
from email_parser import extract_email_headers, extract_email_bodies
from email_parser import extract_email_headers


def test_extract_from_and_reply_to():
    result = extract_email_headers("samples/email_04.eml")

    assert result["sender_address"] == "security@acme-support.example"
    assert result["reply_address"] == "support@acme-help.example"


def test_extract_email_without_reply_to():
    result = extract_email_headers("samples/email_05.eml")

    assert result["sender_address"] == "it@company.example"
    assert result["reply_address"] == ""

def test_extract_from_and_reply_to():
    result = extract_email_headers("samples/email_04.eml")

    assert result["sender_address"] == "security@acme-support.example"
    assert result["reply_address"] == "support@acme-help.example"

def test_extract_email_without_reply_to():
    result = extract_email_headers("samples/email_05.eml")

    assert result["sender_address"] == "it@company.example"
    assert result["reply_address"] == ""

def test_extract_plain_text_body():
    result = extract_email_bodies("samples/email_06.eml")

def test_extract_both_bodies_from_multipart():
    result = extract_email_bodies("samples/email_07.eml")

    assert "Your account requires verification" in result["plain_text"]
    assert "fake-example.com/login" in result["html"]
