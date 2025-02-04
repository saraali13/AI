import random


class SecuritySystem:
    def __init__(self):
        self.components = {}
        for i in range(9):
            key = chr(65 + i)  # Convert number to letter (A to I)
            self.components[key] = random.choice(["Safe", "Vulnerable"])  # Assign status

    def initial_check(self):
        print("\nInitial system status: \n", self.components)

    def final_check(self):
        print("\nFinal System Status: \n", self.components)


class SecurityAgent:

    def __init__(self,system):
        self.system=system
        self.vulnerable_components = []

    def scan_system(self):
        for i in self.system.components:
            if self.system.components[i] == "Vulnerable":
                self.vulnerable_components.append(i)

        print("\nScan Report:")
        for i in self.system.components:
            if i in self.vulnerable_components:
                print(f"{i}: Warning Vulnerable!")

            else:
                print(f"{i}: Safe!")

    def patch_system(self):
        for i in self.vulnerable_components:
            self.system.components[i] = "Safe"
        print("\nPatched all vulnerable components!")


sec_system = SecuritySystem()
sec_agent = SecurityAgent(sec_system)

# Printing the initial state
sec_system.initial_check()
# scanning the system
sec_agent.scan_system()
# patching vulnerabilities
sec_agent.patch_system()
# printing the final state of the system after patching
sec_system.final_check()
