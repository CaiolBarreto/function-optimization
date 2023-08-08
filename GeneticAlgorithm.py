from genetic_functions import (
    initialize_population,
    fitness,
    selection,
    crossover,
    mutation,
)


def genetic_algorithm(
    pop_size,
    num_generations,
    mutation_rate,
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

        best_chromosome = population[fitness_values.index(max(fitness_values))]
        print(
            f"Generation {generation}: Best Value = {current_function(best_chromosome)}"
        )

        new_population = [best_chromosome]

        for _ in range(pop_size // 2):
            first_parent, second_parent = selection(population, fitness_values)
            first_offspring, second_offspring = crossover(first_parent, second_parent)
            first_offspring = mutation(
                first_offspring, mutation_rate, min_value, max_value
            )
            second_offspring = mutation(
                second_offspring, mutation_rate, min_value, max_value
            )
            new_population.extend([first_offspring, second_offspring])

        population = new_population

    best_chromosome = max(population, key=lambda x: fitness(x, current_function))
    global_min_point = best_chromosome
    global_min_value = current_function(global_min_point)
    print("Global Minimum Value:", global_min_value)
    return global_min_value
