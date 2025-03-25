html_content = """
<!DOCTYPE html>
<html>
<head><title>Cybersecurity Report</title></head>
<body>
    <h1>Security Assessment Report</h1>
    <h2>Findings:</h2>
    <ul>
        <li>Open Ports: 22, 80, 443</li>
        <li>Vulnerabilities: SQL Injection, XSS</li>
        <li>Recommendations: Patch vulnerabilities, enforce strong authentication</li>
    </ul>
</body>
</html>
"""

with open("security_report.html", "w") as file:
    file.write(html_content)

print("[INFO] Report saved as 'security_report.html'"
