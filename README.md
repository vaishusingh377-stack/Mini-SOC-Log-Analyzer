
# Mini SOC Log Analyzer

## About the Project
Mini SOC Log Analyzer is a Python-based cybersecurity project
that analyzes authentication logs and detects suspicious login
activity using rule-based detection.

It simulates a basic Security Operations Center (SOC) workflow.

## Features
- Reads authentication logs from an external file.
- Detects repeated failed login attempts.
- Groups failed attempts by source IP address.
- Assigns HIGH and CRITICAL severity levels.
- Recommends investigation actions.
- Generates a CSV incident report.

## Technologies Used
- Python
- File Handling
- Dictionaries
- CSV Module
- Security Log Analysis

## Project Structure
Mini-SOC-Log-Analyzer/
├── log_analyzer.py
├── security.log
├── incident_report.csv
└── README.md

## How to Run

1. Install Python 3.
2. Download or clone this repository.
3. Open the project folder in VS Code.
4. Run the following command:

python log_analyzer.py

## Detection Rules
- Fewer than 3 failed attempts: No high-severity alert.
- 3–4 failed attempts: HIGH severity.
- 5 or more failed attempts: CRITICAL severity.

These thresholds are configurable demonstration rules,
not universal indicators of an attack.

## Learning Outcomes
- Basic security log analysis.
- Rule-based threat detection.
- Python file handling.
- Incident reporting.
- Security alert classification.

## Limitations
This project uses simulated authentication logs.
It does not monitor live systems or confirm that an attack
has occurred. Alerts require further investigation.

## Future Improvements
- Add a graphical dashboard.
- Support additional log formats.
- Detect more suspicious authentication patterns.
- Add automated unit tests.
