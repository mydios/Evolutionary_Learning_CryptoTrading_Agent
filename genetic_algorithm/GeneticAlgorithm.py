from abc import ABC, abstractmethod
from typing import Callable

from deap import creator, tools
from deap.base import Fitness, Toolbox
from deap.tools import selBest


class GeneticAlgorithm(ABC):
    def __init__(self, gene_initializer: Callable, evaluation_function: Callable,
                 crossover_parents: Callable, mutate_individual: Callable, optimization_target: str = 'minimum',
                 individual_datastructure: object = list, natural_selector: Callable = selBest):
        self.gene_initializer = gene_initializer
        self.evaluation_function = evaluation_function
        self.crossover_parents = crossover_parents
        self.mutate_individual = mutate_individual
        self.individual_datastructure = individual_datastructure
        self.toolbox = Toolbox()

        creator.create("Fitness", Fitness, weights=(-1.0 if optimization_target == 'minimum' else 1.0,))
        creator.create("Individual", self.individual_datastructure, fitness=creator.Fitness)
        self.toolbox.register("mate", self.crossover_parents)
        self.toolbox.register("mutate", self.mutate_individual)
        self.toolbox.register("evaluate", self.evaluation_function)
        self.toolbox.register("select", natural_selector)
        self.toolbox.register("individual", self.gene_initializer, creator.Individual)
        self.toolbox.register("population", tools.initRepeat, list, self.toolbox.individual)

    @abstractmethod
    def run(self, initial_population_size: int, number_of_generations: int, crossover_probability: float,
            mutation_probability: float):
        pass
