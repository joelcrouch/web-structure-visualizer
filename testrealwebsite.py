from web_scraper.scraper import Scraper
from web_scraper.visualizer import Visualizer
from bs4 import BeautifulSoup

URL="https://news.ycombinator.com/"

scraper=Scraper(URL)
soup=scraper.fetch()
print("page Title: ",soup.title.text)
articles=soup.find_all("a",class_="titlelink")

print("\nTop articles on Hacker News:")
for idx,article in enumerate(articles, start=1):
    print(f"{idx}. {article.text} ({article['href']})")

print("\nWebpage Structure:\n")
scraper.print_structure()
    
visualizer=Visualizer(URL)
visualizer.highlight_elements(articles)