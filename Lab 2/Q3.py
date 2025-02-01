import random


class BackupManagementSystem:
    def __init__(self):
        self.tasks = {}
        for i in range(5):
            self.tasks[i] = random.choice(['Completed', 'Failed'])

    def initial_status(self):
        print("\nInitial Backup Status: \n", self.tasks)

    def final_status(self):
        print("\nFinal Backup Status: \n", self.tasks)


class BackupManagementAgent(BackupManagementSystem):

    def __init__(self):
        super().__init__()
        self.failed_tasks = []

    def scan_system(self):
        for i in self.tasks:
            if self.tasks[i] == "Failed":
                self.failed_tasks.append(i)

        print("\nScan Report:")
        for i in self.tasks:
            if i in self.failed_tasks:
                print(f"{i}: Backup Failed!")
            else:
                print(f"{i}: Backup Completed!")

    def retry_backup(self):
        for i in self.failed_tasks:
            self.tasks[i] = "Completed"


BM_Agent = BackupManagementAgent()

# printing the initial state
BM_Agent.initial_status()
# scanning the system status
BM_Agent.scan_system()
# Retrying the failed backup
BM_Agent.retry_backup()
# printing the final state of the system after retrying
BM_Agent.final_status()
