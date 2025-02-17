import heapq
import random
import time

def update_edge_costs(graph, g_costs, pq):
    """ Randomly updates edge costs and re-evaluates paths dynamically """
    for node in graph:
        for i in range(len(graph[node])):
            neighbor, _, heuristic = graph[node][i]
            new_cost = random.randint(1, 10)  # Assign a new random edge cost
            graph[node][i] = (neighbor, new_cost, heuristic)  # Update cost
            
            # If a better path is found, update priority queue
            if neighbor in g_costs and g_costs[node] + new_cost < g_costs[neighbor]:
                new_g = g_costs[node] + new_cost
                f_value = new_g + heuristic
                heapq.heappush(pq, (f_value, neighbor, new_g))  # Reinsert with new cost
                g_costs[neighbor] = new_g  # Update stored g-cost

def astar_search(graph, start, goal, dynamic_update_interval=3):
    """ Implements A* search with dynamic edge cost updates """
    pq = []  # Priority queue (heap)
    heapq.heappush(pq, (0, start, 0))  # (f-value, node, g-cost)
    
    came_from = {}  # Path reconstruction
    g_costs = {start: 0}  # Store best known g-costs
    visited = set()
    step = 0  # Track time steps

    while pq:
        # Update edges dynamically at set intervals
        if step % dynamic_update_interval == 0:
            update_edge_costs(graph, g_costs, pq)

        f_value, node, g_cost = heapq.heappop(pq)  # Get best node

        if node in visited and g_cost >= g_costs[node]:
            continue  # Skip if we already found a better path to this node

        visited.add(node)  # Mark as visited
        print(f"Visiting: {node}, g-cost: {g_cost}, f-value: {f_value}")

        if node == goal:  # If goal is reached, reconstruct path
            print("Goal reached!")
            path = []
            while node in came_from:
                path.append(node)
                node = came_from[node]
            path.append(start)
            return path[::-1]  # Reverse the path

        # Expand neighbors
        for neighbor, edge_cost, heuristic in graph.get(node, []):
            new_g = g_cost + edge_cost  # Calculate new g-cost

            # If this path is better, update and add to queue
            if neighbor not in g_costs or new_g < g_costs[neighbor]:
                g_costs[neighbor] = new_g
                f_value = new_g + heuristic
                heapq.heappush(pq, (f_value, neighbor, new_g))
                came_from[neighbor] = node  # Store path info

        step += 1  # Increment step count

    print("Goal not reachable!")
    return None

# Example graph (dynamic edges)
graph = {
    'A': [('B', 5, 9), ('C', 8, 5)],
    'B': [('D', 10, 4)],
    'C': [('E', 3, 7)],
    'D': [('F', 7, 5)],
    'E': [('F', 2, 1)],
    'F': []
}

print("\nA* Search with Dynamic Edge Costs:")
path = astar_search(graph, 'A', 'F')
if path:
    print("Optimal Path Found:", path)
else:
    print("No Path Found")
