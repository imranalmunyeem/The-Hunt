from modules.scanners.email_scanner import EmailScanner
from modules.scanners.social_media_scanner import SocialMediaScanner
from modules.scanners.tech_stack_scanner import TechStackScanner
from modules.scanners.virustotal_scanner import VirusTotalScanner
from modules.scanners.hibp_scanner import HIBPScanner
from modules.scanners.github_leak_scanner import GitHubLeakScanner

class PassiveScanner:
    def __init__(self, target):
        self.target = target
        self.scanners = {
            "Email Harvesting": EmailScanner(target),
            "Social Media Presence": SocialMediaScanner(target),
            "Tech Stack Identification": TechStackScanner(target),
            "VirusTotal Check": VirusTotalScanner(target),
            "HIBP Breach Check": HIBPScanner(target),
            "GitHub Leaks": GitHubLeakScanner(target)
        }

    def scan(self, selected_info):
        results = {}
        for info in selected_info:
            if info in self.scanners:
                results[info] = self.scanners[info].scan()
        return results
