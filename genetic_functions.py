import random


def initialize_population(pop_size, dimensions, min_value, max_value):
    return [
        [random.uniform(min_value, max_value) for _ in range(dimensions)]
        for _ in range(pop_size)
    ]


def fitness(chromosome, current_function):
    return 1 / (1 + current_function(chromosome))


def selection(population, fitness_values):
    total_fitness = sum(fitness_values)
    probabilities = [fitness_value / total_fitness for fitness_value in fitness_values]
    return random.choices(population, weights=probabilities, k=2)


def crossover(first_parent, second_parent):
    crossover_point = random.randint(1, len(first_parent) - 1)
    first_offspring = first_parent[:crossover_point] + second_parent[crossover_point:]
    second_offspring = second_parent[:crossover_point] + first_parent[crossover_point:]
    return first_offspring, second_offspring


def mutation(chromosome, mutation_rate, min_value, max_value):
    mutated_chromosome = chromosome[:]
    if random.random() < mutation_rate:
        index_to_mutate = random.randint(0, len(mutated_chromosome) - 1)
        mutated_chromosome[index_to_mutate] = random.uniform(min_value, max_value)
    return mutated_chromosome
