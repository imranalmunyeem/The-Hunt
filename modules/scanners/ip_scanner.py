import socket
from modules.base_scanner import BaseScanner

class IPScanner(BaseScanner):
    def scan(self):
        try:
            ip = socket.gethostbyname(self.target)
            return {"IP Address": ip}
        except Exception as e:
            return f"Error: {e}"
