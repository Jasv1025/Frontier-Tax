from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No file provided"}), 400

    try:
        df = pd.read_excel(file)
        result = {
            "rows": len(df),
            "columns": list(df.columns)
        }
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=8000, host="127.0.0.1")