from flask import Flask, request, render_template
import os
import subprocess
from datetime import datetime

app = Flask(__name__)
OUTPUT_DIR = "./output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        git_url = request.form["git_url"]
        tag = request.form["tag"]
        repo = request.form["repo"]

        image_ref = f"{repo}:{tag}"
        ts = datetime.now().strftime("%Y%m%d%H%M%S")
        base_filename = f"{repo.replace('/', '_')}_{ts}"

        sbom_txt = os.path.join(OUTPUT_DIR, f"{base_filename}.sbom")
        sbom_json = os.path.join(OUTPUT_DIR, f"{base_filename}.json")
        vuln_json = os.path.join(OUTPUT_DIR, f"{base_filename}_vulns.json")

        try:
            subprocess.run(["syft", image_ref, "-o", "syft-table"], stdout=open(sbom_txt, "w"), check=True)
            subprocess.run(["syft", image_ref, "-o", "cyclonedx-json"], stdout=open(sbom_json, "w"), check=True)
            subprocess.run(["grype", f"sbom:{sbom_json}", "-o", f"table={vuln_json}"], check=True)
        except subprocess.CalledProcessError as e:
            return f"エラー: {e}"

        return f"出力完了: {sbom_txt}, {sbom_json}, {vuln_json}"
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
