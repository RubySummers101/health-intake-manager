from datetime import datetime

class SymptomEntry:
    def __init__(self, symptom, severity, note=""):
        self.symptom = symptom
        self.severity = severity  # 1–10 scale
        self.note = note
        self.timestamp = datetime.now()

    def __str__(self):
        return f"[{self.timestamp.strftime('%Y-%m-%d %H:%M')}] {self.symptom} (Severity: {self.severity}) - {self.note}"