from typing import Callable

from deap.algorithms import eaSimple
from deap.tools import selBest

from genetic_algorithm.GeneticAlgorithm import GeneticAlgorithm


class SimpleGeneticAlgorithm(GeneticAlgorithm):
    def __init__(self, gene_initializer: Callable, evaluation_function: Callable,
                 crossover_parents: Callable, mutate_individual: Callable, optimization_target: str = 'minimum',
                 individual_datastructure: object = list, natural_selector: Callable = selBest):
        super().__init__(gene_initializer, evaluation_function, crossover_parents, mutate_individual,
                         optimization_target, individual_datastructure, natural_selector)

    def run(self, initial_population_size: int, number_of_generations: int, crossover_probability: float,
            mutation_probability: float):
        population = self.toolbox.population(1000)

        final_population, _ = eaSimple(population, self.toolbox, crossover_probability, mutation_probability,
                                       number_of_generations)
        return selBest(final_population, 1)
