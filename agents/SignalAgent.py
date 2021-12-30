from collections import deque
from typing import List, Callable

import numpy as np

from data_records.CandleStick import CandleStick
from features.FeatureExtractor import FeatureExtractor
from models.Model import Model


class SignalAgent:
    def __init__(self, model: Model, positive_signal_threshold: float, feature_extractors: List[FeatureExtractor],
                 buy_callback: Callable, time_window: int = 8):
        self.model: Model = model
        self.positive_signal_threshold: float = positive_signal_threshold
        self.feature_extractors: List[FeatureExtractor] = feature_extractors
        self.buy_callback = buy_callback
        self.time_window: int = time_window if time_window > 0 else None
        self.candlestick_history: deque[CandleStick] = deque(maxlen=time_window - 1) if time_window > 0 else None

    def _extract_features(self, candlestick: CandleStick) -> List[float]:
        features: List[float] = []
        for feature_extractor in self.feature_extractors:
            candlesticks: List[CandleStick] = list(self.candlestick_history) if self.time_window else []
            candlesticks.append(candlestick)
            features += feature_extractor.extract_features(candlesticks)
        if self.time_window:
            self.candlestick_history.append(candlestick)
        return features

    def process(self, candlestick: CandleStick):
        features: List[float] = self._extract_features(candlestick)
        signal: float = self.model.execute(np.array(features))[0]
        if signal > self.positive_signal_threshold:
            self.buy_callback(candlestick)
