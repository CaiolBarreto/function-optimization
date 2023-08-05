import random
import math

def ackley_function(x):
    a = 20
    b = 0.2
    c = 2 * math.pi
    sum1 = sum([xi ** 2 for xi in x])
    sum2 = sum([math.cos(c * xi) for xi in x])
    n = len(x)
    term1 = -a * math.exp(-b * math.sqrt(sum1 / n))
    term2 = -math.exp(sum2 / n)
    return term1 + term2 + a + math.exp(1)

def initialize_population(pop_size, num_variables, min_value, max_value):
    return [[random.uniform(min_value, max_value) for _ in range(num_variables)] for _ in range(pop_size)]

def fitness(chromosome):
    return 1 / (1 + ackley_function(chromosome))

def selection(population, fitness_values):
    total_fitness = sum(fitness_values)
    probabilities = [fitness_value / total_fitness for fitness_value in fitness_values]
    return random.choices(population, weights=probabilities, k=2)

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
    offspring2 = parent2[:crossover_point] + parent1[crossover_point:]
    return offspring1, offspring2

def mutation(chromosome, mutation_rate, min_value, max_value):
    mutated_chromosome = chromosome[:]
    for i in range(len(mutated_chromosome)):
        if random.random() < mutation_rate:
            mutated_chromosome[i] = random.uniform(min_value, max_value)
    return mutated_chromosome

def genetic_algorithm(pop_size, num_generations, mutation_rate, num_variables, min_value, max_value):
    population = initialize_population(pop_size, num_variables, min_value, max_value)

    for generation in range(num_generations):
        fitness_values = [fitness(chromosome) for chromosome in population]

        best_chromosome = population[fitness_values.index(max(fitness_values))]
        print(f"Generation {generation}: Best Value = {ackley_function(best_chromosome)}")

        new_population = []

        for _ in range(pop_size // 2):
            parents = selection(population, fitness_values)
            offspring1, offspring2 = crossover(*parents)
            offspring1 = mutation(offspring1, mutation_rate, min_value, max_value)
            offspring2 = mutation(offspring2, mutation_rate, min_value, max_value)
            new_population.extend([offspring1, offspring2])

        population = new_population

    best_chromosome = max(population, key=fitness)
    global_min_point = best_chromosome
    global_min_value = ackley_function(global_min_point)
    print("\nGlobal Minimum Point:", global_min_point)
    print("Global Minimum Value:", global_min_value)

if __name__ == "__main__":
    population_size = 50
    num_generations = 100
    mutation_rate = 0.1
    num_variables = 30
    min_value, max_value = -5, 5

    genetic_algorithm(population_size, num_generations, mutation_rate, num_variables, min_value, max_value)
