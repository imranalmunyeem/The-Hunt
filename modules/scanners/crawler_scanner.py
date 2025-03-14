import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from modules.base_scanner import BaseScanner

class WebCrawlerScanner(BaseScanner):
    def __init__(self, target, depth=1):
        super().__init__(target)
        self.depth = depth
        self.visited_urls = set()

    def crawl(self, url, current_depth):
        if current_depth > self.depth or url in self.visited_urls:
            return []

        try:
            response = requests.get(url, timeout=5)
            soup = BeautifulSoup(response.text, "html.parser")
            self.visited_urls.add(url)

            links = [urljoin(url, link.get("href")) for link in soup.find_all("a", href=True)]
            return links[:10]  # Limit to 10 links per page for efficiency
        except Exception:
            return []

    def scan(self):
        crawled_data = self.crawl(f"https://{self.target}", 1)
        return crawled_data if crawled_data else "No links found or site is restricted."
