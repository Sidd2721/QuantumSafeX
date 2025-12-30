from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        message = request.form.get("message")

        # --- SIMULATED PQC FLOW (for demo) ---
        result = {
            "public_key": "Kbh4Vtzv3wGeFF...Q==",
            "secret_key": "VDpszB3mNFPjQ...==",
            "encrypted": "kFUsv8aLE...==",
            "signature": "RV15N4aD...==",
            "status": "Signature is valid! Message decrypted successfully"
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
