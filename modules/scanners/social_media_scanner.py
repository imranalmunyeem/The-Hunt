import requests
from modules.base_scanner import BaseScanner

class SocialMediaScanner(BaseScanner):
    def scan(self):
        platforms = ["facebook", "twitter", "linkedin", "instagram"]
        results = {}
        for platform in platforms:
            url = f"https://www.{platform}.com/{self.target}"
            response = requests.get(url)
            if response.status_code == 200:
                results[platform] = url
        return results
