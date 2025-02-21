class Search:
    def __init__(self, soup):
        self.soup = soup

    def search_by_value(self, value):
        # Search for the value in text or attributes
        results = []
        for tag in self.soup.find_all():
            if value in tag.text or any(value in str(attr) for attr in tag.attrs.values()):
                results.append(tag)
        return results
