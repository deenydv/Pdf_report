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

print("[INFO] Report sent via email"
