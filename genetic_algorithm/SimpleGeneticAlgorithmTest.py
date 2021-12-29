import unittest

import numpy as np
from deap import tools

from genetic_algorithm.SimpleGeneticAlgorithm import SimpleGeneticAlgorithm


class SimpleGeneticAlgorithmTest(unittest.TestCase):
    simple_genetic_algorithm = None

    def setUp(self) -> None:
        self.simple_genetic_algorithm = SimpleGeneticAlgorithm(crossover_parents=self.crossover_parents,
                                                               evaluation_function=self.evaluation_function,
                                                               mutate_individual=self.mutate_individual,
                                                               gene_initializer=self.gene_initializer)

    def test_learn_mean_function(self):
        print(self.simple_genetic_algorithm.run(100, 50, 0.5, 0.5))

    @staticmethod
    def mutate_individual(individual):
        for i in range(len(individual)):
            if np.random.rand() < 0.5:
                continue
            negative_mutation = (np.random.rand() < 0.5)
            mutation_amount = np.random.rand() / 1000  # in range (0, 0.001)
            if negative_mutation:
                mutation_amount *= -1
            individual[i] += mutation_amount
        return (individual,)

    @staticmethod
    def crossover_parents(parent_1, parent_2):
        return tools.cxTwoPoint(parent_1, parent_2)

    @staticmethod
    def evaluation_function(individual):
        normalization_error = np.abs(np.sum(individual) - 1.0)
        equality_error = np.sum(np.abs(np.array(individual) - 1 / 4))
        return (normalization_error + equality_error,)

    @staticmethod
    def gene_initializer(container):
        c = container()
        for _ in range(4):
            c.append(np.random.rand())
        return c


if __name__ == '__main__':
    unittest.main()
