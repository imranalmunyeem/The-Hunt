import requests
from modules.base_scanner import BaseScanner

class GitHubLeakScanner(BaseScanner):
    def scan(self):
        query = f"{self.target} password OR API key OR credentials"
        search_url = f"https://github.com/search?q={query}&type=code"

        return f"Manually check: {search_url} (GitHub blocks automated searches)"
