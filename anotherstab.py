from bs4 import BeautifulSoup
import requests
from collections import defaultdict
import re

class WebpageAnalyzer:
    def __init__(self):
        self.structure = []
        self.patterns = defaultdict(int)
    
    def analyze_url(self, url):
        """Analyze webpage structure from a given URL."""
        try:
            response = requests.get(url)
            response.raise_for_status()
            return self.analyze_html(response.text)
        except requests.RequestException as e:
            return f"Error fetching URL: {str(e)}"
    
    def analyze_html(self, html_content):
        """Analyze webpage structure from HTML content."""
        soup = BeautifulSoup(html_content, 'html.parser')
        self.structure = []
        self.patterns.clear()
        
        # Analyze head section
        self.analyze_head(soup.head)
        
        # Analyze body section
        self.analyze_body(soup.body)
        
        # Identify repeating patterns
        self.identify_patterns(soup)
        
        return self.generate_report()
    
    def analyze_head(self, head):
        """Analyze the head section of the webpage."""
        if not head:
            return
        
        head_elements = []
        for child in head.children:
            if child.name:
                head_elements.append(child.name)
        
        self.structure.append({
            'section': 'head',
            'elements': head_elements
        })
    
    def analyze_body(self, body):
        """Analyze the body section of the webpage."""
        if not body:
            return
        
        def get_structure(element, depth=0):
            if not hasattr(element, 'name') or not element.name:
                return None
            
            structure = {
                'tag': element.name,
                'classes': element.get('class', []),
                'id': element.get('id', ''),
                'children': []
            }
            
            for child in element.children:
                child_structure = get_structure(child, depth + 1)
                if child_structure:
                    structure['children'].append(child_structure)
            
            return structure
        
        self.structure.append({
            'section': 'body',
            'structure': get_structure(body)
        })
    
    def identify_patterns(self, soup):
        """Identify repeating patterns in the webpage."""
        # Look for common repeating structures
        patterns = {
            'lists': soup.find_all(['ul', 'ol']),
            'tables': soup.find_all('table'),
            'articles': soup.find_all('article'),
            'sections': soup.find_all('section')
        }
        
        for pattern_type, elements in patterns.items():
            if elements:
                for element in elements:
                    # Get the structure of first child as template
                    if element.find():
                        template = self.get_element_structure(element.find())
                        similar_elements = len(element.find_all(template['tag']))
                        if similar_elements > 1:
                            self.patterns[f"{pattern_type}_{element.name}"] = {
                                'count': similar_elements,
                                'template': template
                            }
    
    def get_element_structure(self, element):
        """Get the structure of a single element."""
        if not element or not element.name:
            return None
        
        return {
            'tag': element.name,
            'classes': element.get('class', []),
            'attributes': [attr for attr in element.attrs.keys() if attr not in ['class']]
        }
    
    def generate_report(self):
        """Generate a formatted report of the webpage structure."""
        report = []
        
        # Add head section
        head_section = next((s for s in self.structure if s['section'] == 'head'), None)
        if head_section:
            report.append("HEAD SECTION:")
            report.append("├── Elements:")
            for element in head_section['elements']:
                report.append(f"│   └── {element}")
        
        # Add body structure
        body_section = next((s for s in self.structure if s['section'] == 'body'), None)
        if body_section:
            report.append("\nBODY SECTION:")
            self._add_structure_to_report(body_section['structure'], report, prefix="├── ")
        
        # Add repeating patterns
        if self.patterns:
            report.append("\nREPEATING PATTERNS:")
            for pattern_name, pattern_info in self.patterns.items():
                report.append(f"├── {pattern_name.replace('_', ' ').title()}:")
                report.append(f"│   ├── Count: {pattern_info['count']}")
                report.append(f"│   └── Template Structure: {pattern_info['template']['tag']}")
                if pattern_info['template']['classes']:
                    report.append(f"│       └── Classes: {', '.join(pattern_info['template']['classes'])}")
        
        return "\n".join(report)
    
    def _add_structure_to_report(self, structure, report, prefix="", is_last=False):
        """Recursively add structure to the report."""
        if not structure:
            return
        
        connector = "└── " if is_last else "├── "
        report.append(f"{prefix}{connector}{structure['tag']}")
        
        if structure['classes']:
            class_prefix = prefix + ("    " if is_last else "│   ")
            report.append(f"{class_prefix}└── Classes: {' '.join(structure['classes'])}")
        
        for i, child in enumerate(structure['children']):
            child_prefix = prefix + ("    " if is_last else "│   ")
            self._add_structure_to_report(child, report, child_prefix, i == len(structure['children']) - 1)

# Example usage
analyzer = WebpageAnalyzer()
report = analyzer.analyze_url('https://example.com')
print(report)