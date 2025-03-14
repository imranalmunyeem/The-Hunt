import requests
import re
from modules.base_scanner import BaseScanner

class EmailScanner(BaseScanner):
    def scan(self):
        try:
            response = requests.get(f"https://{self.target}")
            emails = set(re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", response.text))
            return list(emails)
        except Exception as e:
            return f"Error: {e}"
