import random


class HospitalDeliveryRobotTask:
    def __init__(self, layout, med, patient, curr_sit):
        self.environment = layout
        self.medicine = med
        self.patient_schedule = patient
        self.critical_situation = curr_sit
        self.current_location = "Nurse Station"
        self.current_medicine = None
        self.current_patient_id = None

    def move_to(self, loc):
        print(f"Moving from {self.current_location} to {loc}")
        self.current_location = loc

    def pick_medicine(self, med):
        if med in self.medicine:
            print(f"Picking {med} from Medicine Storage")
            self.current_medicine = med
        else:
            print(f"{med} not found in Medicine Storage")

    def scan_patient_id(self, room):
        print(f"Scanning patient ID for {room}")
        self.current_patient_id = random.randint(1000, 9999)
        print(f"Scanned patient ID: {self.current_patient_id}")

    def deliver_medicine(self, room):
        if self.current_medicine:
            print(f"Delivering {self.current_medicine} to {room}")
        else:
            print("No medicine to be delivered")

    def alert_staff(self):
        if self.critical_situation:
            print("Alert Sent !!")
            self.critical_situation = False


class HospitalDeliveryRobot:
    def __init__(self, task, room):
        self.task = task
        self.room = room

    def execute_task(self):
        if self.room in self.task.patient_schedule:
            print(f"\nStarting task for {self.room}:\n")
            required_medicine = self.task.patient_schedule[self.room]
            if required_medicine:
                self.task.move_to("Medicine Storage")
                self.task.pick_medicine(required_medicine)
                self.task.move_to(self.room)
                self.task.scan_patient_id(self.room)
                self.task.deliver_medicine(self.room)
                if self.task.critical_situation:
                    self.task.alert_staff()

        else:
            print(f"No schedule found for {self.room}")


hospital_layout = ["Nurse Station", "Room 101", "Room 102", "Room 103", "Medicine Storage"]
medicines = ["Painkiller", "Antibiotics", "Vaccine"]

patient_schedule = {
    "Room 101": "Painkiller",
    "Room 102": "Antibiotics",
    "Room 103": "Vaccine"
}

# Instantiate robot and execute tasks
T1 = HospitalDeliveryRobotTask(hospital_layout, medicines, patient_schedule, True)
Task1 = HospitalDeliveryRobot(T1, "Room 101")
Task1.execute_task()
print("\n")
T2 = HospitalDeliveryRobotTask(hospital_layout, medicines, patient_schedule, False)
Task2 = HospitalDeliveryRobot(T2, "Room 204")
Task2.execute_task()
print("\n")
T3 = HospitalDeliveryRobotTask(hospital_layout, medicines, patient_schedule, False)
Task3 = HospitalDeliveryRobot(T3, "Room 103")
Task3.execute_task()
print("\n")
