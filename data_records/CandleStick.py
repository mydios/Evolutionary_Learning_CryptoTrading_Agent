class CandleStick:
    def __init__(self, price_open: float, price_close: float, price_high: float, price_low: float):
        self.price_open: float = price_open
        self.price_close: float = price_close
        self.price_high: float = price_high
        self.price_low: float = price_low
