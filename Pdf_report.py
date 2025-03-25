from fpdf import FPDF

class PDFReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Cybersecurity Assessment Report", ln=True, align="C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

pdf = PDFReport()
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.cell(0, 10, "Findings:", ln=True)
pdf.multi_cell(0, 10, "- Open ports found: 22, 80, 443\n- Vulnerabilities detected: SQL Injection, XSS\n- Recommendations: Patch vulnerabilities, enforce strong authentication.")

pdf.output("security_report.pdf")
print("[INFO] Report saved as 'security_report.pdf'"
