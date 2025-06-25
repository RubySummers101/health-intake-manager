from datetime import datetime

class SymptomEntry:
    def __init__(self, symptom, severity, note="", timestamp=None): 

        self.symptom = symptom
        self.severity = severity  # 1–10 scale
        self.note = note
        self.timestamp = timestamp or datetime.now()

    def __str__(self):
        return f"[{self.timestamp.strftime('%Y-%m-%d %H:%M')}] {self.symptom} (Severity: {self.severity}) - {self.note}"
    
    def to_dict(self):
        return {
            "symptom": self.symptom, 
            "severity": self.severity,
            "note": self.note,
            "timestamp": self.timestamp.isoformat()
        }
    
    @staticmethod
    def from_dict(data):
        timestamp = datetime.fromisoformat(data["timestamp"])
        return SymptomEntry(
            symptom=data["symptom"],
            severity=data["severity"],
            note=data.get("note", ""),
            timestamp=timestamp
        )