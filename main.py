from patient import Patient
from symptom_entry import SymptomEntry
from health_log import HealthLog

if __name__ == "__main__":
    patient = Patient("Brenden Riley", 38, "Female")

    log = HealthLog(patient)
    log.add_entry(SymptomEntry("Chest Tightness", 7, "Lasted 2 hours"))
    log.add_entry(SymptomEntry("Fatigue", 8, "After standing for 10 mins"))

    log.print_log()