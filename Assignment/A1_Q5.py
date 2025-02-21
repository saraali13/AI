from queue import PriorityQueue

romania_map = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu': 80},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Rimnicu': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Pitesti': {'Rimnicu': 97, 'Bucharest': 101, 'Craiova': 138},
    'Craiova': {'Drobeta': 120, 'Rimnicu': 146, 'Pitesti': 138},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Mehadia': {'Drobeta': 75, 'Timisoara': 70},
    'Timisoara': {'Arad': 118, 'Mehadia': 70},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}

heuristics = {
    'Arad': 366, 'Zerind': 374, 'Oradea': 380, 'Sibiu': 253, 'Fagaras': 176,
    'Rimnicu': 193, 'Pitesti': 100, 'Craiova': 160, 'Drobeta': 242,
    'Mehadia': 241, 'Timisoara': 329, 'Bucharest': 0, 'Giurgiu': 77,
    'Urziceni': 80, 'Hirsova': 151, 'Eforie': 161, 'Vaslui': 199,
    'Iasi': 226, 'Neamt': 234
}

def bfs(start, goal):
    queue = [(start, [start], 0)]
    visited = set()

    while queue:
        node, path, cost = queue.pop(0)
        if node == goal:
            return path, cost

        if node not in visited:
            visited.add(node)
            for neighbor, step_cost in romania_map[node].items():
                queue.append((neighbor, path + [neighbor], cost + step_cost))

    return None, float('inf')

def ucs(start, goal):
    pq = PriorityQueue()
    pq.put((0, start, [start]))

    while not pq.empty():
        cost, node, path = pq.get()
        if node == goal:
            return path, cost

        for neighbor, step_cost in romania_map[node].items():
            pq.put((cost + step_cost, neighbor, path + [neighbor]))

    return None, float('inf')

def gbfs(start, goal):
    pq = PriorityQueue()
    pq.put((heuristics[start], start, [start], 0))

    while not pq.empty():
        _, node, path, cost = pq.get()
        if node == goal:
            return path, cost

        for neighbor, step_cost in romania_map[node].items():
            pq.put((heuristics[neighbor], neighbor, path + [neighbor], cost + step_cost))

    return None, float('inf')

def iddfs(start, goal, depth):
    def dls(node, goal, path, cost, limit):
        if node == goal:
            return path, cost
        if limit <= 0:
            return None, float('inf')

        for neighbor, step_cost in romania_map[node].items():
            new_path, new_cost = dls(neighbor, goal, path + [neighbor], cost + step_cost, limit - 1)
            if new_path:
                return new_path, new_cost
        return None, float('inf')

    for limit in range(depth):
        result = dls(start, goal, [start], 0, limit)
        if result[0]:
            return result
    return None, float('inf')

def compare_algorithms(start, goal):
    results = {
        "BFS": bfs(start, goal),
        "UCS": ucs(start, goal),
        "GBFS": gbfs(start, goal),
        "IDDFS": iddfs(start, goal, depth=20)
    }

    sorted_results = sorted(results.items(), key=lambda x: x[1][1])  # Sort by cost
    print("\n=== Comparison of Algorithms ===")
    for algo, (path, cost) in sorted_results:
        print(f"{algo}: Path = {path}, Cost = {cost}")



start_city = "Arad"
end_city = "Bucharest"
compare_algorithms(start_city, end_city)
