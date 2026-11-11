from detection import check_reply_to_mismatch

def test_same_domain():
    result = check_reply_to_mismatch(
        "security@company.example",
        "support@company.example"
    )

    assert result is False

def test_different_domains():
    result = check_reply_to_mismatch(
        "security@company.example",
        "attacker@fake.example"
    )

    assert result is True

def test_missing_reply_to():
    result = check_reply_to_mismatch(
        "sucurity@company.example",
        None
    )

    assert result is None

def test_missing_sender():
    result = check_reply_to_mismatch(
        None,
        "support@company.example"
    )

    assert result is None

def test_invalid_email_format():
    result = check_reply_to_mismatch(
        "invalid-email",
        "support@company.example"
    )

    assert result is None