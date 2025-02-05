from bs4 import BeautifulSoup
import requests
#Use requests to fetch the page content and BeautifulSoup to parse it.
class Scraper:
    def __init__(self, url):
        self.url = url
        self.soup = None

    def fetch(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            self.soup = BeautifulSoup(response.text, 'html.parser')
        else:
            raise Exception(f"Failed to fetch page: {response.status_code}")
        return self.soup
