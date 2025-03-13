import whois
from modules.base_scanner import BaseScanner

class WhoisScanner(BaseScanner):
    def scan(self):
        try:
            data = whois.whois(self.target)
            return data.text
        except Exception as e:
            return f"Error: {e}"
