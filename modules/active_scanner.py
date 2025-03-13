from modules.scanners.whois_scanner import WhoisScanner
from modules.scanners.dns_scanner import DNSScanner
from modules.scanners.ip_scanner import IPScanner
from modules.scanners.vulnerability_scanner import VulnerabilityScanner
from modules.scanners.shodan_scanner import ShodanScanner

class ActiveScanner:
    def __init__(self, target):
        self.target = target
        self.scanners = {
            "WHOIS Lookup": WhoisScanner(target),
            "DNS Records": DNSScanner(target),
            "IP & Hosting Info": IPScanner(target),
            "Website Vulnerabilities": VulnerabilityScanner(target),
            "Shodan Scan": ShodanScanner(target)
        }

    def scan(self, selected_info):
        results = {}
        for info in selected_info:
            if info in self.scanners:
                results[info] = self.scanners[info].scan()
        return results
