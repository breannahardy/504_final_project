# Prototype: Fibroid Symptom Tracking API

This prototype demonstrates a minimal Flask-based application that accepts patient-reported uterine fibroid symptom data and simulates cloud storage by saving uploaded data as JSON files locally. In the full cloud architecture, this storage layer would be implemented using Google Cloud Storage.

## What This Prototype Does
- Runs a Flask web application
- Accepts uterine fibroid symptom data via a POST request
- Simulates cloud storage by saving uploaded data as JSON files locally

## How to Run

1. Navigate to prototype directory.
2. Install dependencies
```
pip install -r requirements.txt
```
3. Run the application
```python app.py
```
4. The application will run at:
<http://127.0.0.1:5000>

5. Send a POST request to `/upload` with JSON data.

### Example JSON Payload
```
json
{
"patient_id": "123",
"pain_score": 3,
"bleeding_score": 4,
"fatigue_score": 2
}
```