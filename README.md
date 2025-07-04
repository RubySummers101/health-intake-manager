# Health Intake Manager

A personal health tracking system built with Python. This command-line application helps users log and visualize physical symptoms, mood, and sleep patterns using modular, object-oriented design.  
It’s designed to be extensible for future features such as symptom classification and natural language intake summaries.

---

## Features

- Create and manage patient profiles  
- Log physical symptoms with severity and optional notes  
- Track mood and sleep in daily journal entries  
- Automatically save/load data using JSON  
- Generate visual plots of symptom severity, mood, and sleep  
- Clean and modular object-oriented Python code  

---

## Technologies Used

- Python 3.10  
- Git + GitHub (developed in GitHub Codespaces)  
- Object-Oriented Programming (OOP)  
- JSON for persistent data storage  
- Matplotlib for data visualization  

---

## Project Structure

```
health-intake-manager/
├── app.py               # Main application logic and menu system
├── patient.py           # Patient class definition
├── symptom_entry.py     # SymptomEntry class for tracking symptoms
├── health_log.py        # HealthLog class for managing symptom entries
├── journal_entry.py     # JournalEntry class for mood and sleep tracking
├── health_data.json     # Data file for saved logs and journal entries
└── README.md            # Project documentation
```

---

## How to Run

Make sure you have Python 3.10+ and `matplotlib` installed.

```bash
pip install matplotlib
python app.py
```

---

## Example Output

**Health Log:**
```
--- Health Log for Ruby Summers ---
[2025-06-14 12:21] Chest Tightness (Severity: 7) - Lasted 2 hours
[2025-06-14 12:22] Fatigue (Severity: 8) - After standing for 10 mins
```

**Mood and Sleep Charts:**  
- `mood_plot.png`  
- `sleep_plot.png`

**Symptom Severity Chart Example:**  
- `chest_tightness_severity_plot.png`

---

## Future Enhancements

- Natural language processing (NLP) summaries for journal and symptom entries  
- Symptom classification using a machine learning model or LLM  
- Export functionality (PDF or CSV)  
- GUI interface or mobile version  
- Dockerized version for deployment  

---

## Author

**Ruby Summers**  
GitHub: [github.com/RubySummers101](https://github.com/RubySummers101)