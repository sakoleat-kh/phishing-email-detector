
from email_parser import extract_email_headers


def test_extract_from_and_reply_to():
    result = extract_email_headers("samples/email_04.eml")

    assert result["sender_address"] == "security@acme-support.example"
    assert result["reply_address"] == "support@acme-help.example"


def test_extract_email_without_reply_to():
    result = extract_email_headers("samples/email_05.eml")

    assert result["sender_address"] == "it@company.example"
    assert result["reply_address"] == ""
