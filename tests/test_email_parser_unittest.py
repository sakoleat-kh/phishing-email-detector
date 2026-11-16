import unittest

from email_parser import extract_email_headers, extract_email_bodies

class TestEmailParser(unittest.TestCase):
    pass


    def test_normal_email(self):
        result = extract_email_headers("samples/email_04.eml")

        self.assertEqual(
            result["sender_address"],
            "security@acme-support.example"
        )

    def test_multipart_email(self):
        result = extract_email_bodies("samples/email_07.eml")

        self.assertTrue(result["plain_text"])
        self.assertTrue(result["html"])

    def test_missing_reply_to(self):
        result = extract_email_headers("samples/email_05.eml")

        self.assertEqual(
            result["sender_address"],
            "it@company.example"
        )

        self.assertEqual(result["reply_address"], "")

if __name__ == "__main__":
    unittest.main()