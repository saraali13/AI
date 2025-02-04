class FirefightingRobotSystem:
    def __init__(self):
        self.rooms = {'a': ' ', 'b': '🔥', 'c': '🔥', 'd': ' ', 'e': '🔥', 'f': ' ', 'g': '🔥', 'h': ' ', 'j': '🔥'}
        self.path = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j']

    def initial_status(self):
        print("Initial Room Status:", self.rooms)

    def final_status(self):
        print("Final Room Status:", self.rooms)


class FirefightingRobotAgent:

    def __init__(self, system):
        self.system = system

    def move_and_extinguish(self):
        # Move through rooms, extinguishing fires
        for room in self.system.path:
            print(f"Moved to Room {room}")
            if self.system.rooms[room] == '🔥':
                print(f"Extinguishing the Fire detected in Room {room}!!")
                self.system.rooms[room] = ' '
            print(f"Current Status: {self.system.rooms}")


sys=FirefightingRobotSystem()
FFR1 = FirefightingRobotAgent(sys)
sys.initial_status()
FFR1.move_and_extinguish()
sys.final_status()
