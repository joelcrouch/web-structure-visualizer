from collections import Counter
#Traverse the DOM to find all unique elements and their attributes.
class FieldIdentifier:
    def __init__(self, soup):
        self.soup = soup

    def get_unique_tags(self):
        tags = set(tag.name for tag in self.soup.find_all())
        return tags

    def detect_repeating_patterns(self):
        # Count the frequency of parent elements with children
        parent_counts = Counter([tag.parent.name for tag in self.soup.find_all()])
        repeating_parents = [tag for tag, count in parent_counts.items() if count > 5]  # Threshold for repetition maybe change this to 2 b/c repeat >1  
        return repeating_parents

    def infer_field_names(self):
        # Infer field names based on attributes or placeholder text
        fields = {}
        for tag in self.soup.find_all():
            if 'name' in tag.attrs:
                fields[tag.attrs['name']] = tag.name
            elif 'placeholder' in tag.attrs:
                fields[tag.attrs['placeholder']] = tag.name
        return fields
