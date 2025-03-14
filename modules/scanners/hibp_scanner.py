import requests
from modules.base_scanner import BaseScanner
from config import HIBP_API_KEY

class HIBPScanner(BaseScanner):
    def scan(self):
        url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{self.target}"
        headers = {
            "hibp-api-key": HIBP_API_KEY,
            "User-Agent": "OSINT-Tool"
        }
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return response.json()  # List of breaches
            elif response.status_code == 404:
                return "No breaches found for this email."
            else:
                return f"Error: {response.status_code} - {response.text}"
        except Exception as e:
            return f"Error: {e}"
