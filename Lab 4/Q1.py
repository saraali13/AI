import heapq

class Node:
    def __init__(self, position, visited_goals, parent=None):
        self.position = position
        self.visited_goals = visited_goals  # Set of visited goals
        self.parent = parent
        self.f = 0  # Heuristic value (Manhattan distance to nearest unvisited goal)

    def __lt__(self, other):
        return self.f < other.f  # Priority queue sorting based on heuristic

def manhattan_distance(p1, p2):
    """Calculate Manhattan distance between two points."""
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def best_first_search(maze, start, goals):
    rows, cols = len(maze), len(maze[0])
    all_goals = set(goals)  # Set of all goal positions

    # Priority queue: (heuristic, position, visited_goals)
    frontier = []
    start_node = Node(start, frozenset())  # Initial node with no goals visited
    start_node.f = min(manhattan_distance(start, g) for g in goals)  # Heuristic: distance to nearest goal
    heapq.heappush(frontier, (start_node.f, start_node))

    visited_states = set()  # Track visited (position, visited_goals_set)
    came_from = {}  # Store parent for path reconstruction

    while frontier:
        _, current_node = heapq.heappop(frontier)
        current_pos, visited_goals = current_node.position, current_node.visited_goals

        # If all goals are visited, reconstruct path
        if visited_goals == all_goals:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Reverse path to get correct order

        # Mark state as visited
        state = (current_pos, visited_goals)
        if state in visited_states:
            continue
        visited_states.add(state)

        # Explore neighbors
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_pos = (current_pos[0] + dx, current_pos[1] + dy)
            if 0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols and maze[new_pos[0]][new_pos[1]] == 0:
                # Update visited goals if a goal is reached
                new_visited_goals = visited_goals | {new_pos} if new_pos in all_goals else visited_goals
                new_state = (new_pos, new_visited_goals)

                if new_state not in visited_states:
                    new_node = Node(new_pos, new_visited_goals, current_node)
                    remaining_goals = all_goals - new_visited_goals  # Find goals not yet visited

                    if remaining_goals:  # If there are unvisited goals
                        distances = [manhattan_distance(new_pos, g) for g in remaining_goals]  
                        min_distance = min(distances)  # Find the nearest goal
                        new_node.f = min_distance  # Set heuristic value to nearest goal distance
                    else:
                        new_node.f = 0  # All goals visited, so no need for further searching

                    heapq.heappush(frontier, (new_node.f, new_node))
                    came_from[new_pos] = current_pos  # Track path

    return None  # No path found

# Example maze (0 = open path, 1 = wall)
maze = [
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)  # Start position
goals = [(2, 2), (4, 4)]  # Multiple goal points

# Find the shortest path covering all goals
path = best_first_search(maze, start, goals)

if path:
    print("Path found:", path)
else:
    print("No path found")
