from abc import ABC, abstractmethod
from typing import List

from data_records.CandleStick import CandleStick


class FeatureExtractor(ABC):

    @abstractmethod
    def extract_feature(self, candlestick: CandleStick) -> float:
        pass

    def extract_features(self, candlesticks: List[CandleStick]) -> List[float]:
        features = []
        for candlestick in candlesticks:
            features.append(self.extract_feature(candlestick))
        return features
