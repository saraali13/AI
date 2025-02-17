import heapq

def heuristic(current, goal):
    """Calculate the heuristic (Euclidean distance) between two points."""
    return ((current[0] - goal[0]) ** 2 + (current[1] - goal[1]) ** 2) ** 0.5

def greedy_best_first_search(start, delivery_points):
    """Find an optimized delivery route using Greedy Best-First Search considering both time and distance."""
    route = []  # Stores the final delivery route
    current_location = start  # Start from the initial location
    priority_queue = []  # Min-heap to prioritize locations
    visited = set()  # To avoid visiting the same location twice
    
    # Push all delivery points into a priority queue based on both time window and distance
    for point in delivery_points:
        location, time_window = point
        distance = heuristic(current_location, location)  # Compute distance from the start
        priority = (time_window, distance)  # Tuple: (time priority, distance)
        heapq.heappush(priority_queue, (priority, location))
    
    while priority_queue:
        _, next_point = heapq.heappop(priority_queue)  # Pick the best (priority, distance) location
        
        if next_point not in visited:
            visited.add(next_point)
            route.append(next_point)
            current_location = next_point  # Move to the new location
            
            # Rebuild the priority queue based on the new current location
            temp_queue = []
            while priority_queue:
                _, loc = heapq.heappop(priority_queue)
                new_distance = heuristic(current_location, loc)
                new_priority = (time_window, new_distance)
                heapq.heappush(temp_queue, (new_priority, loc))
            priority_queue = temp_queue  # Update the priority queue with new distances
    
    return route

# Example Usage
start_location = (0, 0)
delivery_points = [
    ((4, 3), 3),  # Delivery point (x, y) with time window priority
    ((1, 2), 1),
    ((5, 5), 5),
    ((2, 1), 2)
]

optimized_route = greedy_best_first_search(start_location, delivery_points)
print("Optimized Delivery Route:", optimized_route)
