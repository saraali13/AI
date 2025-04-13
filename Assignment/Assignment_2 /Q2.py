import random

# Task times
tasks = [5, 8, 4, 7, 6, 3, 9]
# Facility capacities (in hours per day)
capacities = [24, 30, 28]
# Cost matrix: task × facility
costs = [
    [10, 12, 9],
    [15, 14, 16],
    [8, 9, 7],
    [12, 10, 13],
    [14, 13, 12],
    [9, 8, 10],
    [11, 12, 13]
]

# Parameters
POPULATION_SIZE = 6
GENERATIONS = 50
CROSSOVER_RATE = 0.8
MUTATION_RATE = 0.2


# Create a random valid chromosome
def create_chromosome():
    while True:
        chromo = [random.randint(0, 2) for _ in tasks]
        if is_valid(chromo):
            return chromo


# Check if total hours assigned to each facility is within limits
def is_valid(chromo):
    loads = [0, 0, 0]
    for task, facility in enumerate(chromo):
        loads[facility] += tasks[task]
    for i in range(3):
        if loads[i] > capacities[i]:
            return False
    return True


# Fitness = 1 / (total cost + penalty)
def fitness(chromo):
    total_cost = 0
    loads = [0, 0, 0]
    for task, facility in enumerate(chromo):
        total_cost += tasks[task] * costs[task][facility]
        loads[facility] += tasks[task]

    penalty = 0
    for i in range(3):
        if loads[i] > capacities[i]:
            penalty += (loads[i] - capacities[i]) ** 2

    return 1 / (total_cost + 1000 * penalty)


# Selection using Roulette Wheel
def select(population):
    scores = [fitness(chromo) for chromo in population]
    total = sum(scores)
    probs = [s / total for s in scores]
    return random.choices(population, weights=probs, k=2)


# One-point crossover
def crossover(parent1, parent2):
    if random.random() > CROSSOVER_RATE:
        return parent1[:]
    point = random.randint(1, len(tasks) - 1)
    child = parent1[:point] + parent2[point:]
    return child if is_valid(child) else parent1[:]


# Mutation: swap two task assignments
def mutate(chromo):
    if random.random() > MUTATION_RATE:
        return chromo
    i, j = random.sample(range(len(tasks)), 2)
    chromo[i], chromo[j] = chromo[j], chromo[i]
    return chromo if is_valid(chromo) else chromo


# Run the Genetic Algorithm
def run_ga():
    population = [create_chromosome() for _ in range(POPULATION_SIZE)]

    for _ in range(GENERATIONS):
        new_population = []
        while len(new_population) < POPULATION_SIZE:
            p1, p2 = select(population)
            child = crossover(p1, p2)
            child = mutate(child)
            new_population.append(child)
        population = new_population

    # Return best solution
    best = max(population, key=fitness)
    return best


# Run
best_solution = run_ga()
print("Best Task Assignment:", best_solution)

# Final stats
loads = [0, 0, 0]
total_cost = 0
for task, facility in enumerate(best_solution):
    loads[facility] += tasks[task]
    total_cost += tasks[task] * costs[task][facility]

print("Facility Loads:", loads)
print("Total Cost:", total_cost)
