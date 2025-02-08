class UtilityBasedAgent:
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
            return env.ucs_search(percept, self.goal)


class Environment:
    def __init__(self, graph):
        self.graph = graph

    def get_percept(self, node):
        return node

    def ucs_search(self, start, goal):
        frontier=[(start,0)]
        visited=set()
        cost_so_far={start:0}
        came_from={start:None}

        while frontier:
            frontier.sort(key=lambda x:x[1])
            current_node,current_cost= frontier.pop(0)
            if current_node in visited:
                continue
            visited.add(current_node)

            if current_node==goal:
                path=[]

                while current_node is not None:
                    path.append(current_node)
                    current_node=came_from[current_node]

                path.reverse()
                print(f"Goal {goal} found!\n{path}\nTotal Cost: {current_cost}")
                return
            for neighbour,cost in self.graph[current_node].items():
                new_cost=current_cost+cost
                if neighbour not in cost_so_far or new_cost <cost_so_far[neighbour]:
                    cost_so_far[neighbour]=new_cost
                    came_from[neighbour]=current_node
                    frontier.append((neighbour,new_cost))
        print("Goal not found")



def run_agent(agent, env, start):
    percept = env.get_percept(start)
    action = agent.act(percept, env)
    print(action)


tree = {
    'A': {'B': 2, 'C': 1},
    'B': {'D': 4, 'E': 3},
    'C': {'F': 1, 'G': 5},
    'D': {'H': 2},
    'E': {},
    'F': {'I': 6},
    'G': {},
    'H': {},
    'I': {}
}

start_node = "A"
goal_node = "G"

agent1 = UtilityBasedAgent(goal_node)
env1 = Environment(tree)

run_agent(agent1, env1, start_node)
