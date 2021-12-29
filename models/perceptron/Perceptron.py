from typing import Callable

import numpy as np
from numpy import ndarray

from models.Model import Model


class Perceptron(Model):
    def __init__(self, n_inputs: int, weights: ndarray = None, activation_function: Callable = None):
        super().__init__(n_inputs, weights)
        self.activation_function: Callable = activation_function
        if activation_function is None:
            self.activation_function = lambda x: 1 / (1 + np.exp(x))

    def execute(self, inputs: ndarray) -> ndarray:
        super().execute(inputs)
        return self.activation_function(np.dot(self.weights, inputs))
