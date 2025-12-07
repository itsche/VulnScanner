# controller/scanner_controller.py
from flask import Flask, render_template, request
from model.scanner_model import scan_url, scan_batch
import os

app = Flask(__name__, template_folder="../templates")

# Ensure reports folder exists
os.makedirs("reports", exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    batch_results = None
    urls_input = None
    if request.method == "POST":
        urls_input = request.form.get("urls")
        if urls_input:
            urls = [u.strip() for u in urls_input.split(",") if u.strip()]
            if len(urls) == 1:
                result = scan_url(urls[0])
            else:
                batch_results = scan_batch(urls)
    return render_template("scanner_view.html", result=result, batch_results=batch_results, urls_input=urls_input)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
