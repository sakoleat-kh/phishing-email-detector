from detection import check_reply_to_mismatch

from pathlib import Path
from urllib.parse import urlparse
import re


def analyze_email(file_path):
    """Extract email information and check for URL domain mismatches."""

    print("\n" + "=" * 60)
    print(f"Analyzing: {file_path.name}")
    print("=" * 60)

    # Read the email file
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Split content into individual lines
    lines = content.splitlines()

    # Initialize extracted values
    sender = None
    subject = None
    actual_url = None
    displayed_url = None
    reply_to = None

    # Extract sender and subject
    for line in lines:
        if line.startswith("From:"):
            sender = line.split(":", 1)[1].strip()

        if line.startswith("Subject:"):
            subject = line.split(":", 1)[1].strip()
        
        if line.startswith("Reply-To:"):
            reply_to = line.split(":", 1)[1].strip()

    # Extract actual destination and displayed URL
    for index, line in enumerate(lines):

        if "href=" in line:
            result = re.search(r'href="([^"]+)"', line)

            if result:
                actual_url = result.group(1)

                # Extract displayed URL from the next line
                if index + 1 < len(lines):
                    displayed_url = lines[index + 1].strip()

                break

    # Display extracted information
    print(f"Sender: {sender}")
    print(f"Subject: {subject}")
    print(f"Reply-To: {reply_to}")

    # Compare sender and Reply-To domains
    if sender and reply_to:
        sender_domain = sender.split("@")[-1].lower()
        reply_domain = reply_to.split("@")[-1].lower()

        print("\nFrom domain:", sender_domain)
        print("Reply-To domain:", reply_domain)

        if sender_domain != reply_domain:
            print("\n[WARNING] From and Reply-To domains do not match!")
        else:
            print("\nNo From/Reply-To domain mismatch detected.")
    else:
        print("\n[INFO] From or Reply-To header is missing.")

    print(f"\nActual destination: {actual_url}")
    print(f"Displayed URL: {displayed_url}")

    # Compare URL domains
    if actual_url and displayed_url:
        displayed_domain = urlparse(displayed_url).hostname
        actual_domain = urlparse(actual_url).hostname

        print(f"\nDisplayed domain: {displayed_domain}")
        print(f"Actual domain: {actual_domain}")

        if displayed_domain != actual_domain:
            print("\n[WARNING] Potential URL mismatch detected!")
        else:
            print("\nNo URL mismatch detected.")

    else:
        print("\n[ERROR] Could not extract both URLs.")


def main():
    """Process all email samples."""

    samples_directory = Path("samples")

    # Find all text files in samples/
    sample_files = sorted(samples_directory.glob("*.txt"))

    if not sample_files:
        print("No email samples found.")
        return

    print(f"Found {len(sample_files)} email sample(s).")

    # Analyze each email
    for file_path in sample_files:
        analyze_email(file_path)


if __name__ == "__main__":
    main()
