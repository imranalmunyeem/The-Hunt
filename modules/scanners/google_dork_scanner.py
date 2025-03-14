import requests
from modules.base_scanner import BaseScanner

class GoogleDorkScanner(BaseScanner):
    def scan(self):
        dorks = [
            f"site:{self.target} intitle:index.of",
            f"site:{self.target} inurl:admin",
            f"site:{self.target} filetype:log",
            f"site:{self.target} ext:sql",
            f"site:{self.target} intext:'password'"
        ]

        results = {}
        try:
            for dork in dorks:
                search_url = f"https://www.google.com/search?q={dork}"
                results[dork] = f"Google search URL: {search_url}"
            return results
        except Exception as e:
            return f"Error: {e}"
