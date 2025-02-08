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
            return env.dfs_search(percept, self.goal)


class Environment:
    def __init__(self, graph):
        self.graph = graph

    def get_percept(self, node):
        return node

    def dfs_search(self, start, goal):
        visited = []
        stack = []

        visited.append(start)
        stack.append(start)

        while stack:
            node = stack.pop()
            print(f"Visiting: {node}")

            if node == goal:
                return f"Goal {goal} found!"
            for neighbour in reversed(self.graph.get(node, [])):
                if neighbour not in visited:
                    visited.append(neighbour)
                    stack.append(neighbour)

        return "Goal not found"


def run_agent(agent, env, start):
    percept = env.get_percept(start)
    action = agent.act(percept,env)
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
