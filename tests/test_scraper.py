import unittest
from web_scraper.scraper import Scraper

class TestScraper(unittest.TestCase):
    def test_fetch(self):
        scraper = Scraper("https://news.ycombinator.com/")
        soup = scraper.fetch()
        self.assertIsNotNone(soup)  # Ensure we get a valid response

if __name__ == "__main__":
    unittest.main()