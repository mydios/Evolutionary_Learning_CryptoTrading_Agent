import deap.base
import numpy as np

from deap import creator, tools
from deap.base import Toolbox
from deap.algorithms import eaSimple

n_entries = 4
target_weight = 1 / n_entries

creator.create("Fitness", deap.base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.Fitness)

toolbox = Toolbox()

toolbox.register("attr_mean_weight", np.random.rand)

def own_initializer(container, sampler, n):
    res = tools.initRepeat(container, sampler, n)
    res.append(np.random.rand())
    return res

toolbox.register("individual", own_initializer, creator.Individual,
                 toolbox.attr_mean_weight, n_entries)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def eval_mean(individual):
    normalization_error = np.abs(np.sum(individual) - 1.0)
    equality_error = np.sum(np.abs(np.array(individual) - target_weight))
    return (normalization_error + equality_error,)


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


# register the goal / fitness function
toolbox.register("evaluate", eval_mean)

# register the crossover operator
toolbox.register("mate", tools.cxTwoPoint)

# register a mutation operator
toolbox.register("mutate", mutate_individual)

# operator for selecting individuals for breeding the next
# generation: each individual of the current generation
# is replaced by the 'fittest' (best) of three individuals
# drawn randomly from the current generation.
toolbox.register("select", tools.selTournament, tournsize=3)

crossover_probability = 0.5
mutation_probability = 0.5
n_generations = 100

population = toolbox.population(1000)

final_population, _ = eaSimple(population, toolbox, crossover_probability, mutation_probability, n_generations)
best_individual = tools.selBest(final_population, 1)
print(best_individual)
print(len(final_population))
