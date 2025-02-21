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
    
    def get_structure(self):
        """Returns a simplified structure of the webpage"""
        if not self.soup:
            self.fetch_page()
        
        structure = {}
        for tag in self.soup.find_all():
            tag_name = tag.name
            structure[tag_name] = structure.get(tag_name, 0) + 1
        
        return structure  # Dictionary of HTML tags and their counts

    def print_structure(self):
        """Prints the structure in a readable way"""
        structure = self.get_structure()
        print("\nWebpage Structure:\n")
        for tag, count in sorted(structure.items(), key=lambda x: x[1], reverse=True):
            print(f"{tag}: {count}")
