import requests
from modules.base_scanner import BaseScanner
from config import VIRUSTOTAL_API_KEY

class VirusTotalScanner(BaseScanner):
    def scan(self):
        url = f"https://www.virustotal.com/api/v3/domains/{self.target}"
        headers = {"x-apikey": VIRUSTOTAL_API_KEY}
        try:
            response = requests.get(url, headers=headers)
            return response.json()
        except Exception as e:
            return f"Error: {e}"
