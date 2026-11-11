
from email import policy
from email.parser import BytesParser
from email.utils import parseaddr

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
