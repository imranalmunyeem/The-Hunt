import dns.resolver
from modules.base_scanner import BaseScanner

class DNSScanner(BaseScanner):
    def scan(self):
        records = {}
        try:
            for record_type in ["A", "MX", "NS", "TXT", "CNAME"]:
                records[record_type] = [r.to_text() for r in dns.resolver.resolve(self.target, record_type)]
            return records
        except Exception as e:
            return f"Error: {e}"
