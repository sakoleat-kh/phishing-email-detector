
# Phishing Email Detector

A Python-based learning project that analyzes email samples and detects potential phishing indicators by comparing displayed URLs with their actual hyperlink destinations.

## Project Objective

The goal of this project is to build a simple phishing email detection tool using Python.

The initial version focuses on identifying URL mismatches, where the URL displayed to the user differs from the actual destination embedded in an HTML hyperlink.

## Features

- Read email samples from text files.
- Extract sender and subject information.
- Extract actual hyperlink destinations using regular expressions.
- Extract displayed URLs.
- Compare displayed and actual URL domains.
- Detect potential URL mismatches.
- Process multiple email samples automatically.
- Handle emails with missing URLs without crashing.

## Project Structure

```text
phishing-email-detector/
├── samples/
│   ├── email_01.txt
│   ├── email_02.txt
│   └── email_03.txt
├── .gitignore
├── main.py
└── README.md
```

## Requirements

- Python 3.10 or later
- No external Python packages required.

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd phishing-email-detector
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

## Usage

Run the detector:

```bash
python main.py
```

The program automatically finds and analyzes all `.txt` files inside the `samples/` directory.

## Detection Logic

The detector compares the hostname of the displayed URL with the hostname of the actual hyperlink destination.

Example:

**Displayed URL:**
```text
https://accounts.acme.example/reset
```

**Actual destination:**
```text
https://acme-verify.example/login
```

**Result:**
```text
[WARNING] Potential URL mismatch detected!
```

If both hostnames match, the program reports:

```text
No URL mismatch detected.
```

If the email does not contain both URLs, the program reports:

```text
[ERROR] Could not extract both URLs.
```

## Test Scenarios

| Sample | Scenario | Expected result |
|---|---|---|
| email_01.txt | Matching URL domains | No mismatch |
| email_02.txt | Different URL domains | Warning |
| email_03.txt | No URL present | Error handled safely |

## Current Limitations

This is an initial learning version of the detector.

- It supports the current sample email format.
- It checks URL hostname mismatches only.
- It does not yet analyze email headers or sender authentication.
- It does not use machine learning.
- A matching hostname does not guarantee that a URL is safe.
- A URL mismatch is a potential phishing indicator, not proof of malicious activity.

## Future Improvements

- Improve HTML email parsing.
- Validate URLs and detect suspicious domains.
- Analyze email headers.
- Add sender authentication checks such as SPF, DKIM, and DMARC.
- Introduce additional phishing detection rules.
- Build automated tests with pytest.
- Generate a risk score for each email.

## Disclaimer

This project is developed for educational and cybersecurity research purposes. All included email samples are fictional.
