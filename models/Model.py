from abc import ABC, abstractmethod

import numpy as np
from numpy import ndarray


class Model(ABC):
    def __init__(self, n_inputs: int, weights: ndarray = None):
        self.n_inputs = n_inputs
        self.weights: ndarray = weights
        if (n_inputs is None) or n_inputs < 0:
            self.n_inputs = 0
        if weights is None:
            self.weights = np.random.uniform(-1 / np.sqrt(self.n_inputs), 1 / np.sqrt(self.n_inputs), self.n_inputs)

    def set_weights(self, weights: ndarray) -> None:
        if weights.ndim != 1 or len(weights) != self.n_inputs:
            raise ValueError(f"Got weights of dimension {np.shape(weights)} but expected {np.shape(self.weights)}")
        else:
            self.weights = weights

    @abstractmethod
    def execute(self, inputs: ndarray) -> ndarray:
        if inputs.ndim != 1 or len(inputs) != self.n_inputs:
            raise ValueError(f"Got inputs of dimension {np.shape(inputs)} but expected {np.shape(self.weights)}")
        pass
