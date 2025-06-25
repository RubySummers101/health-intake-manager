from datetime import datetime

class JournalEntry:
    def __init__(self, mood, sleep_hours, notes="", date=None):
        self.date = date or datetime.now().date()
        self.mood = mood
        self.sleep_hours = sleep_hours
        self.notes = notes

    def __str__(self):
        return (
            f"{self.date} | Mood: {self.mood}/10 | Sleep: {self.sleep_hours}h | Notes: {self.notes}"
        )

    def to_dict(self):
        """Convert this entry into a JSON-friendly dict."""
        return {
            "date": self.date.isoformat(),
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
            date=datetime.fromisoformat(data["date"]).date()
        )
