# AI-Powered Vulnerability Scanner

A simple yet advanced web vulnerability scanner built in Python using Flask.  
Scans single or multiple URLs for common vulnerabilities and missing security headers, and provides risk scores with actionable recommendations.

---

## Features

- **Single & Batch URL Scanning** – Scan one or multiple websites at once.
- **AI Heuristic Scoring** – Simple rule-based scoring for vulnerabilities.
- **Vulnerability Detection**
  - SQL Injection patterns
  - Cross-Site Scripting (XSS)
  - Missing security headers (`X-Frame-Options`, `Content-Security-Policy`, `Strict-Transport-Security`)
- **Risk Labeling** – Low / Medium / High risk badges.
- **Security Recommendations** – Actionable advice based on findings.
- **CSV Reporting** – Automatically generates reports in `reports/` folder.
- **Responsive UI** – Color-coded badges, mobile-friendly, Bootstrap 5.

---

## Folder Structure

VulnScanner/
├─ controller/
│ └─ scanner_controller.py
├─ model/
│ └─ scanner_model.py
├─ templates/
│ └─ scanner_view.html
├─ reports/ # stores CSV reports
├─ init.py
├─ README.md

# AI-Powered Vulnerability Scanner - Setup & Usage

## Clone Repository
```bash
git clone https://github.com/yourusername/VulnScanner.git
cd VulnScanner
Install Dependencies
bash
Copy code
pip install flask requests pandas

Ensure Reports Folder Exists
bash
Copy code
mkdir -p reports

Run the Flask App
bash
Copy code
python -m controller.scanner_controller
Open the preview or navigate to http://127.0.0.1:5000 in your browser.

Use the Scanner
Single URL Scan: Enter one URL in the input field, click Scan.

View the results in the web UI:

Risk badges (Low / Medium / High)
Detected vulnerabilities (SQLi, XSS)
Missing security headers
Recommendations
