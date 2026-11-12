
from email import policy
from email.parser import BytesParser
from email.utils import parseaddr

from html_analyzer import extract_links
from detection import check_reply_to_mismatch


def extract_email_headers(email_path):
    """Parse an EML file and extract sender and Reply-To information."""

    with open(email_path, "rb") as file:
        message = BytesParser(policy=policy.default).parse(file)

    # Extract headers
    sender = message["From"]
    reply_to = message["Reply-To"]

    # Extract names and email addresses
    sender_name, sender_address = parseaddr(str(sender)) if sender else ("", "")
    reply_name, reply_address = parseaddr(str(reply_to)) if reply_to else ("", "")

    return {
        "sender_name": sender_name,
        "sender_address": sender_address,
        "reply_name": reply_name,
        "reply_address": reply_address
    }

def extract_email_bodies(email_path):
    """Extract plain-text and HTML bodies from an EML file."""

    with open(email_path, "rb") as file:
        message = BytesParser(policy=policy.default).parse(file)

    plain_text = None
    html = None

    for part in message.walk():

        if part.get_content_maintype() == "multipart":
            continue

        content_type = part.get_content_type()
        content = part.get_content()

        if not content or not content.strip():
            continue

        if content_type == "text/plain" and plain_text is None:
            plain_text = content

        elif content_type == "text/html" and html is None:
            html = content

    return {
        "plain_text": plain_text,
        "html": html
    }

def analyze_eml(email_path):
    """Display email information and analyze Reply-To mismatch."""

    result = extract_email_headers(email_path)

    print("\nEmail Analysis")
    print("=" * 40)

    print("Sender name:", result["sender_name"])
    print("Sender address:", result["sender_address"] or "Not provided")

    print("Reply-To name:", result["reply_name"])
    print("Reply-To address:", result["reply_address"] or "Not provided")

    mismatch = check_reply_to_mismatch(
        result["sender_address"],
        result["reply_address"]
    )

    if mismatch is True:
        print("\n[WARNING] From and Reply-To domains do not match!")

    elif mismatch is False:
        print("\nNo From/Reply-To domain mismatch detected.")

    else:
        print("\n[INFO] Cannot compare email addresses.")


if __name__ == "__main__":
    analyze_eml("samples/email_04.eml")
    analyze_eml("samples/email_05.eml")

    print("\n--- Email 06 Body ---")
    bodies = extract_email_bodies("samples/email_06.eml")
    print("Plain Text:")
    print(bodies["plain_text"])

    print("\n--- Email 07 Body ---")
    bodies = extract_email_bodies("samples/email_07.eml")
    print("Plain Text:")
    print(bodies["plain_text"])

    print("\nHTML:")
    print(bodies["html"])

    print("\n--- HTML Link Analysis ---")

    bodies = extract_email_bodies("samples/email_07.eml")

    links = extract_links(bodies["html"] or "")

    for link in links:
        print("Displayed text:", link["text"])
        print("Actual URL:", link["url"])