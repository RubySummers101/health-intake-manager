class HealthLog:
    def __init__(self, patient):
        self.patient = patient
        self.entries = []

    def add_entry(self, entry):
        self.entries.append(entry)

    def print_log(self):
        print(f"--- Health Log for {self.patient.name} ---")
        if not self.entries:
            print("No symptom entries found.")
        else:
            for entry in self.entries:
                print(entry)