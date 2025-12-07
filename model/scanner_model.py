# model/scanner_model.py
import re
import requests
import pandas as pd
from datetime import datetime

# Security recommendations
RECOMMENDATIONS = {
    "sql_injection": "Use parameterized queries to prevent SQL injection.",
    "xss": "Sanitize input and use Content Security Policy headers.",
    "X-Frame-Options": "Add X-Frame-Options header to prevent clickjacking.",
    "Content-Security-Policy": "Add CSP header to restrict content sources.",
    "Strict-Transport-Security": "Use HSTS header to enforce HTTPS."
}

def scan_url(url: str) -> dict:
    """
    Scan a single URL for vulnerabilities and assign risk score & recommendations.
    """
    result = {
        "url": url,
        "sql_injection": False,
        "xss": False,
        "missing_headers": [],
        "risk_score": 0,
        "risk_label": "Unknown",
        "recommendations": []
    }

    sql_patterns = [r"' OR 1=1", r"UNION SELECT", r"DROP TABLE", r"--"]

    try:
        response = requests.get(url, timeout=5)
        html = response.text.lower()
        headers = response.headers

        # SQL Injection
        if any(re.search(pattern.lower(), html) for pattern in sql_patterns):
            result["sql_injection"] = True
            result["risk_score"] += 3
            result["recommendations"].append(RECOMMENDATIONS["sql_injection"])

        # XSS
        if "<script>" in html or "onerror=" in html:
            result["xss"] = True
            result["risk_score"] += 3
            result["recommendations"].append(RECOMMENDATIONS["xss"])

        # Check headers
        for header in ["X-Frame-Options", "Content-Security-Policy", "Strict-Transport-Security"]:
            if header not in headers:
                result["missing_headers"].append(header)
                result["risk_score"] += 1
                result["recommendations"].append(RECOMMENDATIONS[header])

        # Minimum risk
        if result["risk_score"] == 0:
            result["risk_score"] = 1

    except Exception as e:
        result["error"] = str(e)
        result["risk_score"] = -1
        return result

    # Risk labeling
    if result["risk_score"] <= 2:
        result["risk_label"] = "Low Risk"
    elif result["risk_score"] <= 5:
        result["risk_label"] = "Medium Risk"
    else:
        result["risk_label"] = "High Risk"

    return result


def scan_batch(urls: list) -> list:
    """
    Scan multiple URLs and return list of results.
    Also saves CSV report.
    """
    results = []
    for url in urls:
        results.append(scan_url(url))

    # Save CSV report
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    df = pd.DataFrame(results)
    df.to_csv(f"reports/scan_report_{timestamp}.csv", index=False)
    return results
