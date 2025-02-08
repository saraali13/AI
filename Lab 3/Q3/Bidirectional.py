from collections import deque

def bidirectional_search_tree(tree, start, goal):
    # Forward BFS: Start -> Goal
    forward_queue = deque([start])
    forward_visited = {start: None}  # To store the path

    # Backward BFS: Goal -> Start
    backward_queue = deque([goal])
    backward_visited = {goal: None}  # To store the path

    while forward_queue and backward_queue:
        # Forward BFS step
        current_forward = forward_queue.popleft()
        if current_forward in backward_visited:
            # Path found: Merge forward and backward paths
            return merge_paths(forward_visited, backward_visited, current_forward)

        for neighbour in tree.get(current_forward, []):
            if neighbour not in forward_visited:
                forward_visited[neighbour] = current_forward
                forward_queue.append(neighbour)

        # Backward BFS step
        current_backward = backward_queue.popleft()
        if current_backward in forward_visited:
            # Path found: Merge forward and backward paths
            return merge_paths(forward_visited, backward_visited, current_backward)

        for neighbour in tree.get(current_backward, []):
            if neighbour not in backward_visited:
                backward_visited[neighbour] = current_backward
                backward_queue.append(neighbour)

    return "Goal not found"

# Simplified Bidirectional Search for Graph
def bidirectional_search_graph(graph, start, goal):
    # Forward BFS: Start -> Goal
    forward_queue = deque([start])
    forward_visited = {start: None}  # To store the path

    # Backward BFS: Goal -> Start
    backward_queue = deque([goal])
    backward_visited = {goal: None}  # To store the path

    while forward_queue and backward_queue:
        # Forward BFS step
        current_forward = forward_queue.popleft()
        if current_forward in backward_visited:
            # Path found: Merge forward and backward paths
            return merge_paths(forward_visited, backward_visited, current_forward)

        for neighbour in graph.get(current_forward, []):
            if neighbour not in forward_visited:
                forward_visited[neighbour] = current_forward
                forward_queue.append(neighbour)

        # Backward BFS step
        current_backward = backward_queue.popleft()
        if current_backward in forward_visited:
            # Path found: Merge forward and backward paths
            return merge_paths(forward_visited, backward_visited, current_backward)

        for neighbour in graph.get(current_backward, []):
            if neighbour not in backward_visited:
                backward_visited[neighbour] = current_backward
                backward_queue.append(neighbour)

    return "Goal not found"

# Helper function to merge paths from forward and backward BFS
def merge_paths(forward_visited, backward_visited, meeting_node):
    # Reconstruct path from start to meeting node
    path = []
    node = meeting_node
    while node is not None:
        path.append(node)
        node = forward_visited[node]
    path.reverse()

    # Reconstruct path from meeting node to goal
    node = backward_visited[meeting_node]
    while node is not None:
        path.append(node)
        node = backward_visited[node]

    return path

# Tree Representation
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': [],
    'F': ['I'],
    'G': [],
    'H': [],
    'I': []
}

# Graph Representation
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B', 'H'],
    'E': ['B'],
    'F': ['C', 'I'],
    'G': ['C'],
    'H': ['D'],
    'I': ['F']
}

# Test Bidirectional Search on Tree
print("Bidirectional Search on Tree:")
result_tree = bidirectional_search_tree(tree, 'A', 'I')
print(f"Path: {result_tree}")

# Test Bidirectional Search on Graph
print("\nBidirectional Search on Graph:")
result_graph = bidirectional_search_graph(graph, 'A', 'I')
print(f"Path: {result_graph}")
