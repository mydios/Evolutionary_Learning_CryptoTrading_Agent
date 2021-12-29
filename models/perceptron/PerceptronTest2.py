import unittest

import numpy as np

from models.perceptron.Perceptron import Perceptron


class PerceptronTest(unittest.TestCase):
    def setUp(self) -> None:
        self.p = Perceptron(2)

    def test_perceptron_creation_no_weights(self):
        self.assertTrue(np.sum(np.abs(self.p.weights) > 0))

    def test_perceptron_execution(self):
        self.p.execute(np.array([1, 2]))


if __name__ == '__main__':
    unittest.main()
