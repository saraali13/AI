import math
import random


def calculate_distance(coord1, coord2):
    """Calculate Euclidean distance between two coordinates"""
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)


def total_distance(route):
    """Calculate total distance of a route"""
    distance = 0
    for i in range(len(route) - 1):
        distance += calculate_distance(route[i], route[i + 1])
    # Return to starting point
    distance += calculate_distance(route[-1], route[0])
    return distance


def hill_climbing(coordinates, max_iterations=1000):
    """Hill climbing algorithm for route optimization"""
    # Create initial random route
    current_route = coordinates.copy()
    random.shuffle(current_route)
    current_distance = total_distance(current_route)

    for _ in range(max_iterations):
        # Generate a neighbor by swapping two random cities
        neighbor = current_route.copy()
        i, j = random.sample(range(len(neighbor)), 2)
        neighbor[i], neighbor[j] = neighbor[j], neighbor[i]

        neighbor_distance = total_distance(neighbor)

        # If the neighbor is better, accept it
        if neighbor_distance < current_distance:
            current_route = neighbor
            current_distance = neighbor_distance

    return current_route, current_distance


# Example delivery points
delivery_points = [
    (0, 0), (1, 5), (2, 3), (5, 2),
    (7, 1), (5, 5), (3, 4), (6, 8),
    (8, 7), (9, 2)
]

optimized_route, total_dist = hill_climbing(delivery_points)
print("Optimized route:", optimized_route)
print("Total distance:", total_dist)
