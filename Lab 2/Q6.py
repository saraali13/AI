class FirefightingRobot:
    def __init__(self):
        self.rooms = {'a': ' ', 'b': '🔥', 'c': '🔥', 'd': ' ', 'e': '🔥', 'f': ' ', 'g': '🔥', 'h': ' ', 'j': '🔥'}
        self.path = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j']

    def initial_status(self):
        print("Initial Room Status:", self.rooms)

    def move_and_extinguish(self):
        # Move through rooms, extinguishing fires
        for room in self.path:
            print(f"Moved to Room {room}")
            if self.rooms[room] == '🔥':
                print(f"Extinguishing the Fire detected in Room {room}!!")
                self.rooms[room] = ' '
            print(f"Current Status: {self.rooms}")

    def final_status(self):
        print("Final Room Status:", self.rooms)

FFR1=FirefightingRobot()
FFR1.initial_status()
FFR1.move_and_extinguish()
FFR1.final_status()
