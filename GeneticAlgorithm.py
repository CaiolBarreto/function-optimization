import random

def initialize_population(pop_size, dimensions, min_value, max_value):
    return [[random.uniform(min_value, max_value) for _ in range(dimensions)] for _ in range(pop_size)]

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
    for index in range(len(mutated_chromosome)):
        if random.random() < mutation_rate:
            mutated_chromosome[index] = random.uniform(min_value, max_value)
    return mutated_chromosome

def genetic_algorithm(
    pop_size,
    num_generations,
    mutation_rate,
    dimensions,
    min_value,
    max_value,
    current_function
):
    population = initialize_population(pop_size, dimensions, min_value, max_value)

    for generation in range(num_generations):
        fitness_values = [fitness(chromosome, current_function) for chromosome in population]

        best_chromosome = population[fitness_values.index(max(fitness_values))]
        print(f"Generation {generation}: Best Value = {current_function(best_chromosome)}")

        new_population = []

        for _ in range(pop_size // 2):
            first_parent, second_parent = selection(population, fitness_values)
            first_offspring, second_offspring = crossover(first_parent, second_parent)
            first_offspring = mutation(first_offspring, mutation_rate, min_value, max_value)
            second_offspring = mutation(second_offspring, mutation_rate, min_value, max_value)
            new_population.extend([first_offspring, second_offspring])

        population = new_population

    best_chromosome = max(population, key=lambda x: fitness(x, current_function))
    global_min_point = best_chromosome
    global_min_value = current_function(global_min_point)
    print("\nGlobal Minimum Point:", global_min_point)
    print("Global Minimum Value:", global_min_value)

