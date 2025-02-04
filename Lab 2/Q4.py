import random


class CyberSecuritySystem:
    def __init__(self):
        self.components = {}
        for i in range(9):
            key = chr(65 + i)  # Convert number to letter (A to I)
            self.components[key] = random.choice(
                ["Safe", "Low Risk Vulnerable", "High Risk Vulnerable"])  # Assign status

    def initial_check(self):
        print("\nInitial system status: \n", self.components)

    def final_check(self):
        print("\nFinal System Status: \n", self.components)


class CyberSecurityAgent:

    def __init__(self, system):
        self.system = system
        self.vulnerable_components = []

    def scan_system(self):
        for i in self.system.components:
            if self.system.components[i] == "Low Risk Vulnerable" or self.system.components[i] == "High Risk Vulnerable":
                self.vulnerable_components.append(i)

        print("\nScan Report:")
        for i in self.system.components:
            if i in self.vulnerable_components:
                print(f"{i}: Warning Vulnerable!")

            else:
                print(f"{i}: Safe!")

    def patch_system(self):

        for i in self.vulnerable_components:
            if self.system.components[i] == "Low Risk Vulnerable":
                self.system.components[i] = "Safe"
            else:
                print(f"{i}: Premium service is required for patching High Risk Vulnerability")
        print("\nPatched all Low Risk Vulnerable components!")


cy_sec_system = CyberSecuritySystem()
cy_sec_agent = CyberSecurityAgent(cy_sec_system)

# Printing the initial state
cy_sec_system.initial_check()
# scanning the system
cy_sec_agent.scan_system()
# patching vulnerabilities
print("\n")
cy_sec_agent.patch_system()
# printing the final state of the system after patching
cy_sec_system.final_check()
