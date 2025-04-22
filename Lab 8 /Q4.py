import numpy as np

states = ['Sunny', 'Cloudy', 'Rainy']
n_states = len(states)

# Transition matrix (example probabilities)
transition_matrix = np.array([
    [0.6, 0.3, 0.1],  # Sunny -> Sunny, Cloudy, Rainy
    [0.4, 0.4, 0.2],  # Cloudy -> Sunny, Cloudy, Rainy
    [0.2, 0.3, 0.5]  # Rainy -> Sunny, Cloudy, Rainy
])


# Simulation function
def simulate_weather(days, start_state):
    current_state = start_state
    sequence = [current_state]
    rainy_days = 1 if current_state == 'Rainy' else 0

    for _ in range(1, days):
        probs = transition_matrix[states.index(current_state)]
        current_state = np.random.choice(states, p=probs)
        sequence.append(current_state)
        if current_state == 'Rainy':
            rainy_days += 1

    return sequence, rainy_days


# Simulate 10 days starting from Sunny
sequence, rainy_count = simulate_weather(10, 'Sunny')
print("Weather sequence:", sequence)
print("Number of rainy days:", rainy_count)

# Monte Carlo simulation to estimate probability of at least 3 rainy days
n_simulations = 10000
count = 0

for _ in range(n_simulations):
    _, rainy_days = simulate_weather(10, 'Sunny')
    if rainy_days >= 3:
        count += 1

probability = count / n_simulations
print(f"\nProbability of at least 3 rainy days in 10 days: {probability:.4f}")
