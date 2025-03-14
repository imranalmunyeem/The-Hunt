import requests
from modules.base_scanner import BaseScanner

class DarkWebScanner(BaseScanner):
    def scan(self):
        dark_web_sources = [
            f"https://ahmia.fi/search/?q={self.target}",
            f"https://onion.live/search/?q={self.target}",
            f"https://darksearch.io/search?q={self.target}"
        ]

        results = {source: f"Check results manually: {source}" for source in dark_web_sources}
        return results
