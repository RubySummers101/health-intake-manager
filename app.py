import json
import os
from patient import Patient
from symptom_entry import SymptomEntry
from health_log import HealthLog
from journal_entry import JournalEntry

DATA_FILE = "health_data.json"

def save_data(patient, log, journal_entries):
    data = {
        "patient": {
            "name": patient.name,
            "age": patient.age,
            "gender": patient.gender
        },
        "entries": [entry.to_dict() for entry in log.entries],
        "journal_entries": [entry.to_dict() for entry in journal_entries]
    }
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)
    print("Data saved to file.")

def load_data():
    if not os.path.exists(DATA_FILE):
        return None, None, []

try:
    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    p = data["patient"]
    patient = Patient(p["name"], p["age"], p["gender"])
    log = HealthLog(patient)

    for entry_data in data.get("entries", []):
        log.add_entry(SymptomEntry.from_dict(entry_data))

    journal_entries = []
    for j_entry_data in data.get("journal_entries", []):
        journal_entries.append(JournalEntry.from_dict(j_entry_data))

    print("Data loaded from file.")
    return patient, log, journal_entries
 
except (json.JSONDecodeError, KeyError, TypeError) as e:
    print("Warning: Failed to load data. Starting fresh.")
    return None, None, []

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
    while True:
        name = input("Enter patient name: ").strip()
        if name:
            break
        print("Name cannot be empty.")

    while True:
        try:
            age = int(input("Enter patient age: "))
            break
        except ValueError:
            print("Please enter a valid number for age.")
            
    gender = get_gender_input()
    return Patient(name, ago, gender)

# Main Logic
patient, log, journal_entries = load_data()

if patient:
    confirm = input(f"Welcome back, {patient.name}! Is this you (Y/N): ").strip().lower()
    if confirm != "y":
        patient = create_patient()
        log = HealthLog(patient)
        journal_entries = []

else:
    patient = create_patient()
    log = HealthLog(patient)
    journal_entries = []

def show_menu():
    print("\nWhat would you like to do?")
    print("1. Add a new symptom entry")
    print("2. View health log")
    print("3. Add a journal entry")
    print("4. View journal entries")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        symptom = input("Symptom name: ")
        try:
            severity = int(input("Severity (1-10): "))
            if not 1 <= severity <=10:
                print("Severity must be between 1 and 10.")
                continue
        except ValueError:
            print("Please enter a number between 1 and 10.")
            continue
        
        note = input("Optional note: ")
        entry = SymptomEntry(symptom, severity, note)
        log.add_entry(entry)
        print(f"Symptom added for patient: {patient.name}")

    elif choice == "2":
        log.print_log()

    elif choice == "3":
        try:
            mood = int(input("Mood (1-10): "))
            sleep_hours = float(input("Hours Slept: "))
        except ValueError:
            print("Invalid Entry. Please enter numbers for mood and sleep.")
            continue
            
        notes = input("Additional notes: ")
        journal_entry = JournalEntry(mood, sleep_hours, notes)
        journal_entries.append(journal_entry)
        print("Journal entry added.")

    elif choice == "4":
        if journal_entries:
            print("\nJournal Entries:\n----------------")
            for entry in journal_entries:
                print(entry)
        else:
            print("No journal entries found.")

    elif choice == "5":
        save_data(patient, log, journal_entries)
        print("Data saved. Exiting. Take care!")
        break

    else:
        print("Invalid choice. Please enter 1-5.")
