class GoalBasedAgent:
    def __init__(self, goal):
        self.goal = goal

    def formulate_goal(self, percept):
        if percept == self.goal:
            return "Goal Reached"
        else:
            return "Searching"

    def act(self, percept, env):
        goal_status = self.formulate_goal(percept)
        if goal_status == "Goal Reached":
            return f"Goal {self.goal} found!"
        else:
            return env.dls_search(percept, self.goal, 3)


class Environment:
    def __init__(self, graph):
        self.graph = graph

    def get_percept(self, node):
        return node

    def dls_search(self, start, goal, depth_limit):
        visited = []

        def dfs(node, depth):
            if depth > depth_limit:
                return None  # limit reached
            visited.append(node)
            if node == goal:
                print(f"Goal {goal} found!")
                return visited
            for neighbour in self.graph.get(node, []):
                if neighbour not in visited:
                    path = dfs(neighbour, depth + 1)

                    if path:
                        return path
            visited.pop()  # backtrack
            return None

        return dfs(start, 0)


def run_agent(agent, env, start):
    percept = env.get_percept(start)
    action = agent.act(percept, env)
    print(action)


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

start_node = "A"
goal_node = "G"

agent1 = GoalBasedAgent(goal_node)
env1 = Environment(tree)

run_agent(agent1, env1, start_node)
