from flask import Flask, request, jsonify
import json
import datetime
import uuid
import os

app = Flask(__name__)

# Simulated Cloud Storage directory
STORAGE_DIR = "simulated_cloud_storage"
os.makedirs(STORAGE_DIR, exist_ok=True)

@app.route("/")
def home():
    return "Fibroid Symptom Tracking Prototype is running."

@app.route("/upload", methods=["POST"])
def upload_symptoms():
    data = request.get_json()

    # Add timestamp
    data["timestamp"] = datetime.datetime.utcnow().isoformat()

    # Create unique filename
    filename = f"symptoms_{uuid.uuid4()}.json"
    filepath = os.path.join(STORAGE_DIR, filename)

    # Save file locally (simulating cloud storage)
    with open(filepath, "w") as f:
        json.dump(data, f)

    return jsonify({
        "message": "Symptom data stored successfully (simulated cloud storage)",
        "file": filepath
    })

if __name__ == "__main__":
    app.run(debug=True)

