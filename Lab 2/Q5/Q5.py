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


class HospitalDeliveryRobot(HospitalDeliveryRobotTask):
    def __init__(self, env, med, patient, curr_sit, room):
        super().__init__(env, med, patient, curr_sit)
        self.room = room

    def execute_task(self):
        if self.room in self.patient_schedule:
            print(f"\nStarting task for {self.room}:\n")
            required_medicine = self.patient_schedule[self.room]
            if required_medicine:
                self.move_to("Medicine Storage")
                self.pick_medicine(required_medicine)
                self.move_to(self.room)
                self.scan_patient_id(self.room)
                self.deliver_medicine(self.room)
                if self.critical_situation:
                    self.alert_staff()

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
Task1 = HospitalDeliveryRobot(hospital_layout, medicines, patient_schedule, True, "Room 101")
Task1.execute_task()
print("\n")
Task2 = HospitalDeliveryRobot(hospital_layout, medicines, patient_schedule, False, "Room 204")
Task2.execute_task()
print("\n")
Task3 = HospitalDeliveryRobot(hospital_layout, medicines, patient_schedule, False, "Room 103")
Task3.execute_task()
print("\n")
