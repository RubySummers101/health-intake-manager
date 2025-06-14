class Patient:
    def __init__(self, name, age, gender, medical_conditions=None):
        self.name = name
        self.age = age
        self.gender = gender
        self.medical_conditions = medical_conditions or []

    def add_condition(self, condition):
        self.medical_conditions.append(condition)

    def summary(self):
        return f"{self.name} ({self.age}, {self.gender}) - Conditions: {', '.join(self.medical_conditions)}"

# Test it
if __name__ == "__main__":
    patient1 = Patient("Brenden Riley", 38, "Female")
    patient1.add_condition("Long COVID")
    patient1.add_condition("POTS")
    print(patient1.summary())