def tsp(current_city, visited, cities, distances, current_cost, min_cost, path, best_path):
    if len(visited) == len(cities): # If all cities are visited, return to the starting city
        total_cost = current_cost + distances[current_city][cities[0]]
        if total_cost < min_cost[0]:
            min_cost[0] = total_cost
            best_path[:] = path[:] + [cities[0]]
        return

    for next_city in cities:
        if next_city not in visited:
            visited.add(next_city)  # Mark as visited
            path.append(next_city)  # Add to path

            # Recur with the new city
            tsp(next_city, visited, cities, distances,
                current_cost + distances[current_city][next_city],
                min_cost, path, best_path)

            # Backtrack (undo the move)
            visited.remove(next_city)
            path.pop()


def traveling_salesman(cities, distances):
    min_cost = [float('inf')]  # Store the minimum cost currently is infinity
    best_path = []  # Store the best path

    visited = {cities[0]}  # Start from the first city
    tsp(cities[0], visited, cities, distances, 0, min_cost, [cities[0]], best_path)

    return best_path, min_cost[0]

cities1 = ['1', '2', '3', '4']
distances1 = {
    '1': {'2': 10, '3': 15, '4': 20},
    '2': {'1': 10, '3': 35, '4': 25},
    '3': {'1': 15, '2': 35, '4': 30},
    '4': {'1': 20, '2': 25, '3': 30}
}

best_path, min_cost = traveling_salesman(cities1, distances1)
print(f"Best Path: {best_path}\nMinimum Cost: {min_cost}")
