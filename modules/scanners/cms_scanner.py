import requests
from modules.base_scanner import BaseScanner

class CMSScanner(BaseScanner):
    def scan(self):
        cms_patterns = {
            "WordPress": "wp-content",
            "Joomla": "Joomla",
            "Drupal": "sites/all/modules",
            "Magento": "Mage",
            "Shopify": "cdn.shopify.com"
        }

        try:
            response = requests.get(f"https://{self.target}", timeout=5)
            detected_cms = [cms for cms, pattern in cms_patterns.items() if pattern.lower() in response.text.lower()]
            
            return detected_cms if detected_cms else "No known CMS detected."
        except Exception as e:
            return f"Error: {e}"
