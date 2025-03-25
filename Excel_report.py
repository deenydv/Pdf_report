import pandas as pd

data = {
    "Category": ["Open Ports", "Vulnerabilities", "Recommendations"],
    "Details": ["22, 80, 443", "SQL Injection, XSS", "Patch vulnerabilities, enforce strong authentication"]
}

df = pd.DataFrame(data)
df.to_excel("security_report.xlsx", index=False)

print("[INFO] Report saved as 'security_report.xlsx'"
