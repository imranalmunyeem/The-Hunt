import shodan
from modules.base_scanner import BaseScanner
from config import SHODAN_API_KEY

class ShodanScanner(BaseScanner):
    def scan(self):
        try:
            api = shodan.Shodan(SHODAN_API_KEY)
            result = api.host(self.target)
            return result
        except Exception as e:
            return f"Error: {e}"
