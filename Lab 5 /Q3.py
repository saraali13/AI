import random
import math
from operator import itemgetter


def calculate_distance(coord1, coord2):
    """Calculate Euclidean distance between two coordinates"""
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)


def route_distance(route, cities):
    """Calculate total distance of a route"""
    distance = 0
    for i in range(len(route)):
        from_city = cities[route[i]]
        to_city = cities[route[(i + 1) % len(route)]]
        distance += calculate_distance(from_city, to_city)
    return distance


def create_individual(cities):
    """Create a random individual (route)"""
    individual = list(range(len(cities)))
    random.shuffle(individual)
    return individual


def create_population(pop_size, cities):
    """Create initial population"""
    return [create_individual(cities) for _ in range(pop_size)]


def selection(population, cities, elite_size):
    """Select parents for next generation using tournament selection"""
    # First rank the population by fitness
    ranked_population = []
    for individual in population:
        distance = route_distance(individual, cities)
        ranked_population.append((individual, distance))

    # Sort by distance (lower is better)
    ranked_population.sort(key=itemgetter(1))

    # Select elite individuals directly
    selection_results = [ind[0] for ind in ranked_population[:elite_size]]

    # Tournament selection for the rest
    for _ in range(len(population) - elite_size):
        tournament = random.sample(ranked_population, 3)  # Tournament size of 3
        tournament.sort(key=itemgetter(1))
        selection_results.append(tournament[0][0])

    return selection_results


def breed(parent1, parent2):
    """Ordered crossover breeding"""
    child = []
    geneA = random.randint(0, len(parent1) - 1)
    geneB = random.randint(0, len(parent1) - 1)

    start_gene = min(geneA, geneB)
    end_gene = max(geneA, geneB)

    # Get the slice from parent1
    child_segment = parent1[start_gene:end_gene]

    # Fill the rest with parent2's genes in order
    child = [gene for gene in parent2 if gene not in child_segment]
    child = child[:start_gene] + child_segment + child[start_gene:]

    return child


def mutate(individual, mutation_rate):
    """Swap mutation"""
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            swap_with = random.randint(0, len(individual) - 1)
            individual[i], individual[swap_with] = individual[swap_with], individual[i]
    return individual


def next_generation(current_gen, cities, elite_size, mutation_rate):
    """Create next generation"""
    selection_results = selection(current_gen, cities, elite_size)
    next_gen = []

    # Keep elites
    next_gen.extend(selection_results[:elite_size])

    # Breed the rest
    for _ in range(len(current_gen) - elite_size):
        parent1, parent2 = random.sample(selection_results, 2)
        child = breed(parent1, parent2)
        next_gen.append(child)

    # Apply mutation
    next_gen = [mutate(ind, mutation_rate) for ind in next_gen]

    return next_gen


def genetic_algorithm(cities, pop_size=50, elite_size=10, mutation_rate=0.01, generations=100):
    """Main genetic algorithm function"""
    population = create_population(pop_size, cities)

    for _ in range(generations):
        population = next_generation(population, cities, elite_size, mutation_rate)

    # Get the best individual
    best_individual = min(population, key=lambda x: route_distance(x, cities))
    best_distance = route_distance(best_individual, cities)

    return best_individual, best_distance


cities = {
    0: (0, 0), 1: (1, 5), 2: (2, 3), 3: (5, 2), 4: (7, 1),
    5: (5, 5), 6: (3, 4), 7: (6, 8), 8: (8, 7), 9: (9, 2)
}

best_route, best_distance = genetic_algorithm(cities)
print("Best route (city indices):", best_route)
print("Best distance:", best_distance)

# Print route with coordinates
print("\nRoute with coordinates:")
for city_idx in best_route:
    print(f"City {city_idx}: {cities[city_idx]}")
print(f"City {best_route[0]}: {cities[best_route[0]]}")  # Return to start
