class BaseScanner:
    def __init__(self, target):
        self.target = target

    def scan(self):
        raise NotImplementedError("Subclasses must implement the scan method.")
