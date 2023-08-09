from genetic_functions import (
    initialize_population,
    fitness,
    mutation,
)


def evolution_strategy(
    pop_size,
    num_generations,
    mutation_rate,
    elitism_size,
    dimensions,
    min_value,
    max_value,
    current_function,
):
    population = initialize_population(pop_size, dimensions, min_value, max_value)

    for generation in range(num_generations):
        fitness_values = [
            fitness(chromosome, current_function) for chromosome in population
        ]

        best_chromosomes = [
            population[i]
            for i in sorted(
                range(len(fitness_values)),
                key=lambda x: fitness_values[x],
                reverse=True,
            )[:elitism_size]
        ]

        new_population = best_chromosomes

        for parent in population:
            offspring = mutation(parent, mutation_rate, min_value, max_value)
            new_population.append(offspring)

        population = new_population

    best_chromosome = max(population, key=lambda x: fitness(x, current_function))
    global_min_point = best_chromosome
    global_min_value = current_function(global_min_point)
    print("Global Minimum Value:", global_min_value)
    return global_min_value
