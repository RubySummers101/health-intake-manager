import json
import os
import matplotlib.pyplot as plt
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
    return Patient(name, age, gender)

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

def plot_symptom_history(log):
    if not log.entries:
        print("No symptom entries to plot.")
        return

    # Group symptoms by name
    symptom_dict = {}
    for entry in log.entries:
        symptom_dict.setdefault(entry.symptom.lower(), []).append(entry)

    for symptom, entries in symptom_dict.items():
        dates = [e.timestamp for e in entries]
        severities = [e.severity for e in entries]

        plt.figure()
        plt.plot(dates, severities, marker='o')
        plt.title(f"{symptom.title()} Severity Over Time")
        plt.xlabel("Date")
        plt.ylabel("Severity (1–10)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.grid(True)

    filename = f"{symptom.lower().replace(' ', '_')}_severity_plot.png"
    plt.savefig(filename)
    print(f"Plot saved as {filename}")

def plot_journal_data(journal_entries):
    if not journal_entries:
        print("No journal entries to plot.")
        return

    dates = [entry.timestamp for entry in journal_entries]
    moods = [entry.mood for entry in journal_entries]
    sleep_hours = [entry.sleep_hours for entry in journal_entries]

    # Plot mood
    plt.figure()
    plt.plot(dates, moods, marker='o', label='Mood (1–10)')
    plt.title("Mood Over Time")
    plt.xlabel("Date")
    plt.ylabel("Mood")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    mood_filename = "mood_plot.png"
    plt.savefig(mood_filename)
    print(f"Mood plot saved as {mood_filename}")

    # Plot sleep
    plt.figure()
    plt.plot(dates, sleep_hours, marker='s', label='Hours Slept')
    plt.title("Sleep Hours Over Time")
    plt.xlabel("Date")
    plt.ylabel("Hours Slept")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    sleep_filename = "sleep_plot.png"
    plt.savefig(sleep_filename)
    print(f"Sleep plot saved as {sleep_filename}")


def show_menu():
    print("\nWhat would you like to do?")
    print("1. Add a new symptom entry")
    print("2. View health log")
    print("3. Add a journal entry")
    print("4. View journal entries")
    print("5. Exit")
    print("6. Plot symptom history")
    print("7. Plot mood and sleep data")

while True:
    show_menu()
    choice = input("Enter your choice (1-7): ")

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

    elif choice == "6":
        plot_symptom_history(log)

    elif choice == "7":
        plot_journal_data(journal_entries)
    else:
        print("Invalid choice. Please enter 1-7.")