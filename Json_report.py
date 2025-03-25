import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

sender_email = "attacker@example.com"
receiver_email = "security_team@example.com"
password = "password"

msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = "Cybersecurity Report"

with open("security_report.pdf", "rb") as file:
    attach = MIMEApplication(file.read(), _subtype="pdf")
    attach.add_header("Content-Disposition", "attachment", filename="security_report.pdf")
    msg.attach(attach)

server = smtplib.SMTP("smtp.example.com", 587)
server.starttls()
server.login(sender_email, password)
server.sendmail(sender_email, receiver_email, msg.as_string())
server.quit()

print("[INFO] Report sent via e

import json

report_data = {
    "open_ports": [22, 80, 443],
    "vulnerabilities": ["SQL Injection", "XSS"],
    "recommendations": ["Patch vulnerabilities", "Enforce strong authentication"]
}

with open("security_report.json", "w") as file:
    json.dump(report_data, file, indent=4)

print("[INFO] Report saved as 'security_report.json'")
