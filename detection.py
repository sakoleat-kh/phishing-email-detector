def check_reply_to_mismatch(sender, reply_to):
    """
    Compare the sender and Reply-To email domains.

    Returns:
        True - Domains are different.
        False - Domais are the same.
        None - One or both email addresses are missing.

    """

    if not sender or not reply_to:
        return None

    sender_parts = sender.split("@")
    reply_parts = reply_to.split("@")

    if len(sender_parts) != 2 or len(reply_parts) != 2:
        return None

    sender_domain = sender_parts[1].lower()
    reply_domain = reply_parts[1].lower()

    return sender_domain != reply_domain