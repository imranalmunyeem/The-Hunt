import requests
from modules.base_scanner import BaseScanner

class TechStackScanner(BaseScanner):
    def scan(self):
        headers = {"User-Agent": "Mozilla/5.0"}
        try:
            response = requests.get(f"https://{self.target}", headers=headers)
            tech_stack = []
            if "wordpress" in response.text.lower():
                tech_stack.append("WordPress")
            if "shopify" in response.text.lower():
                tech_stack.append("Shopify")
            return tech_stack if tech_stack else "Unknown"
        except Exception as e:
            return f"Error: {e}"
