findings = input("Enter findings: ")
recommendations = input("Enter recommendations: ")

report = f"""
Cybersecurity Report
--------------------
Findings:
{findings}

Recommendations:
{recommendations}
"""

with open("cli_security_report.txt", "w") as file:
    file.write(report)

print("[INFO] Report saved as 'cli_security_report.txt'"
