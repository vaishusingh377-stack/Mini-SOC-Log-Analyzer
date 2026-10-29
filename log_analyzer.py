
# Mini SOC Log Analyzer
# Reads security logs from an external file

LOG_FILE = "security.log"
THRESHOLD = 3

failed_attempts = {}

print("===== MINI SOC LOG ANALYZER =====")
print("Reading security logs...\n")

try:
    with open(LOG_FILE, "r") as file:
        security_logs = file.readlines()

    for log in security_logs:
        log = log.strip()

        if not log:
            continue

        print(log)

        if "LOGIN_FAILED" in log and "ip=" in log:
            ip = log.split("ip=")[1].split()[0]
            failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

    print("\n===== SECURITY ALERTS =====")

    alert_found = False
    incident_reports = []

    for ip, attempts in failed_attempts.items():
        if attempts >= THRESHOLD:
            alert_found = True

            if attempts >= 5:
                severity = "CRITICAL"
                action = "Investigate immediately and review account activity."
            else:
                severity = "HIGH"
                action = "Investigate the source IP and review authentication logs."

            print(f"\n[{severity}] Suspicious login activity")
            print(f"Source IP: {ip}")
            print(f"Failed attempts: {attempts}")
            print(f"Recommended action: {action}")
            incident_reports.append({
    "source_ip": ip,
    "failed_attempts": attempts,
    "severity": severity,
    "recommended_action": action
})

    if not alert_found:
        print("No suspicious login activity detected.")
        
    import csv

    with open("incident_report.csv", "w", newline="") as report_file:
        fieldnames = [
            "source_ip",
            "failed_attempts",
            "severity",
            "recommended_action"
        ]

        writer = csv.DictWriter(
            report_file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(incident_reports)

    print("\nIncident report saved as incident_report.csv")


except FileNotFoundError:
    print(f"ERROR: {LOG_FILE} was not found.")
    print("Make sure it is in the same folder as this Python file.")
