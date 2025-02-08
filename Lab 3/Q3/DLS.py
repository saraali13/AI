def dls(node, goal, depth, path, graph):
    if depth == 0:
        return False
    if node == goal:
        path.append(node)
        return True
    if node not in graph:
        return False
    for child in graph[node]:
        if dls(child, goal, depth - 1, path, graph):
            path.append(node)
            return True
    return False


def iterative_deepening(start, goal, max_depth, graph):
    for depth in range(max_depth + 1):
        print(f"Depth: {depth}")
        path = []
        if dls(start, goal, depth, path, graph):
            print("\nPath to goal:", " → ".join(reversed(path)))
            return
    print("Goal not found within depth limit.")


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

# Test Iterative Deepening
start_node = 'A'
goal_node = 'I'
max_search_depth = 3
iterative_deepening(start_node, goal_node, max_search_depth, tree)
