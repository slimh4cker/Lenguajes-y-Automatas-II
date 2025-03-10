import os


class InvoiceCounter:
    def __init__(self, counter_file='invoice_counter.txt', prefix='FRUIT-', initial=0):
        self.counter_file = counter_file
        self.prefix = prefix
        self.initial = initial
        self.current = self._load_counter()

    def _load_counter(self):
        if os.path.exists(self.counter_file):
            try:
                with open(self.counter_file, 'r') as f:
                    return int(f.read().strip())
            except (ValueError, IOError):
                return self.initial
        return self.initial

    def _save_counter(self):
        with open(self.counter_file, 'w') as f:
            f.write(str(self.current))

    def get_next(self):
        self.current += 1
        self._save_counter()
        return f"{self.prefix}{self.current:03d}"  # Formato: FRUIT-001, FRUIT-002, etc.


invoice_counter = InvoiceCounter()
