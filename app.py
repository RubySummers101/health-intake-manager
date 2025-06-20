import json
import os
from patient import Patient
from symptom_entry import SymptomEntry
from health_log import HealthLog

DATA_FILE = "health_data.json"

def save_data(patient, log):
    data = {
        "patient": {
            "name": patient.name,
            "age": patient.age,
            "gender": patient.gender
        },
        "entries": [entry.to_dict() for entry in log.entries]
    }
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)
    print("Data saved to file.")

def load_data():
    if not os.path.exists(DATA_FILE):
        return None, None

    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    p = data["patient"]
    patient = Patient(p["name"], p["age"], p["gender"])

    log = HealthLog(patient)
    for entry_data in data["entries"]:
        log.add_entry(SymptomEntry.from_dict(entry_data))

    print("Data loaded from file.")
    return patient, log

def get_gender_input():
    valid_genders = {
        "m": "Male", "male": "Male",
        "f": "Female", "female": "Female",
        "nb": "Non-binary", "non-binary": "Non-binary",
        "n": "Non-binary", "nonbinary": "Non-binary",
        "other": "Other", "o": "Other"
    }

    while True:
        gender_input = input("Enter patient gender (M/F/NB/Other): ").strip().lower()
        if gender_input in valid_genders:
            return valid_genders[gender_input]
        else:
            print("Invalid input. Please enter M, F, NB, or Other.")

def create_patient():
    print("Let's create a new patient profile.")
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    gender = get_gender_input()

    patient = Patient(name, age, gender)
    return patient

# Try to load saved data
patient, log = load_data()

# If no data found, prompt to create a new profile
if not patient:
    patient = create_patient()
    log = HealthLog(patient)


def show_menu():
    print("\n What would you like to do?")
    print("1. Add a new symptom entry")
    print("2. View health log")
    print("3. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        symptom = input("Symptom name: ")
        severity = int(input("Severity (1-10): "))
        note = input("Optional note: ")
        entry = SymptomEntry(symptom, severity, note)
        log.add_entry(entry)
        print("Symptom added!")

    elif choice == "2":
        log.print_log()

    elif choice == "3":
        save_data(patient, log)
        print("Exiting. Take care!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

