from datetime import datetime

class JournalEntry:
    def __init__(self, mood, sleep_hours, notes="", timestamp=None):
        self.timestamp = timestamp or datetime.now()
        self.mood = mood
        self.sleep_hours = sleep_hours
        self.notes = notes

    def __str__(self):
        return (
             f"{self.timestamp.strftime('%Y-%m-%d %H:%M')} | Mood: {self.mood}/10 | Sleep: {self.sleep_hours}h | Notes: {self.notes}"
        )

    def to_dict(self):
        """Convert this entry into a JSON-friendly dict."""
        return {
            "timestamp": self.timestamp.isoformat(),
            "mood": self.mood,
            "sleep_hours": self.sleep_hours,
            "notes": self.notes
        }

    @staticmethod
    def from_dict(data):
        """Rebuild a JournalEntry from a dict."""
        return JournalEntry(
            mood=data["mood"],
            sleep_hours=data["sleep_hours"],
            notes=data.get("notes", ""),
            timestamp=datetime.fromisoformat(data["timestamp"])
        )
