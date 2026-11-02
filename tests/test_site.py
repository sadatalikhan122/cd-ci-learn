from pathlib import Path
import unittest

SITE_FILE = Path(__file__).resolve().parents[1] / "site" / "index.html"


class WebsiteTests(unittest.TestCase):
    def test_website_file_exists(self):
        self.assertTrue(SITE_FILE.exists(), "site/index.html is missing")

    def test_expected_heading(self):
        html = SITE_FILE.read_text(encoding="utf-8")
        self.assertIn("<h1>Hello!</h1>", html)

    def test_button_is_present(self):
        html = SITE_FILE.read_text(encoding="utf-8")
        self.assertIn('id="actionButton"', html)


if __name__ == "__main__":
    unittest.main()
