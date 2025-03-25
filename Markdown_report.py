report = """# Cybersecurity Assessment Report

## Findings:
- **Open Ports:** 22, 80, 443
- **Vulnerabilities:** SQL Injection, XSS
- **Recommendations:**  
  - Patch vulnerabilities  
  - Enforce strong authentication
"""

with open("security_report.md", "w") as file:
    file.write(report)

print("[INFO] Report saved as 'security_report.md'"
