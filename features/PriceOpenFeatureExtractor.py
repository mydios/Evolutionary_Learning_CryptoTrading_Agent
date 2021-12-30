from data_records.CandleStick import CandleStick
from features.FeatureExtractor import FeatureExtractor


class PriceOpenFeatureExtractor(FeatureExtractor):
    def extract_feature(self, candlestick: CandleStick) -> float:
        return candlestick.price_open
