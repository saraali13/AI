import random


class LoadBalancerSystem:
    def __init__(self):
        self.servers = {}
        for i in range(5):
            self.servers[i] = random.choice(['Underloaded', 'Balanced', 'Overloaded'])

    def initial_status(self):
        print("\nInitial Servers Status: \n", self.servers)

    def final_status(self):
        print("\nFinal Servers Status: \n", self.servers)


class LoadBalancerAgent(LoadBalancerSystem):

    def __init__(self):
        super().__init__()
        self.overloaded_servers = []
        self.underloaded_servers = []

    def scan_system(self):
        for i in self.servers:
            if self.servers[i] == "Overloaded":
                self.overloaded_servers.append(i)
            elif self.servers[i] == "Underloaded":
                self.underloaded_servers.append(i)

        print("\nScan Report:")
        for i in self.servers:
            if i in self.overloaded_servers:
                print(f"{i}: Overloaded server!")
            elif i in self.underloaded_servers:
                print(f"{i}: Underloaded server!")
            else:
                print(f"{i}: Balanced!")

    def balance_loader(self):
        for i in self.overloaded_servers:
            if self.underloaded_servers:
                j = self.underloaded_servers.pop()
                self.servers[i] = "Balanced"
                self.servers[j] = "Balanced"
                print(f"Balance is loaded from {i} to {j}")


LB_Agent = LoadBalancerAgent()

# printing the initial state
LB_Agent.initial_status()
# scanning the system status
LB_Agent.scan_system()
# Balancing the load
LB_Agent.balance_loader()
# printing the final state of the system after balancing
LB_Agent.final_status()
