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

# Test IDDFS on Tree
print("IDDFS on Tree:")
iterative_deepening("A", "I", 3, tree)

# Test IDDFS on Graph
print("\nIDDFS on Graph:")
iterative_deepening('A', 'I', 4, graph)
