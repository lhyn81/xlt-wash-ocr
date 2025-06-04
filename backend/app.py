from flask import Flask, jsonify
from flask_cors import CORS # Import CORS

app = Flask(__name__)
CORS(app) # Enable CORS for all routes

@app.route('/<taskid>')
def get_task_details(taskid):
    # Mock data for now, as per TASK.md
    mock_data = {
        "taskID": taskid,
        "car-id": "1122",
        "begintime": 1702060386,
        "endtime": 1702060386,
        "carrages": 12,
        "details": [
            {
                "carrage-id": "01",
                "image": ["01-A.jpg", "01-B.jpg"],
                "score": [0.8, 0.2]
            },
            {
                "carrage-id": "02",
                "image": ["02-A.jpg", "02-B.jpg"],
                "score": [0.8, 0.2]
            },
            {
                "carrage-id": "03",
                "image": ["03-A.jpg", "03-B.jpg"],
                "score": [0.7, 0.3]
            },
            {
                "carrage-id": "04",
                "image": ["04-A.jpg", "04-B.jpg"],
                "score": [0.9, 0.1]
            },
            {
                "carrage-id": "05",
                "image": ["05-A.jpg", "05-B.jpg"],
                "score": [0.6, 0.4]
            },
            {
                "carrage-id": "06",
                "image": ["06-A.jpg", "06-B.jpg"],
                "score": [0.5, 0.5]
            },
            {
                "carrage-id": "07",
                "image": ["07-A.jpg", "07-B.jpg"],
                "score": [0.85, 0.15]
            },
            {
                "carrage-id": "08",
                "image": ["08-A.jpg", "08-B.jpg"],
                "score": [0.75, 0.25]
            },
            {
                "carrage-id": "09",
                "image": ["09-A.jpg", "09-B.jpg"],
                "score": [0.95, 0.05]
            },
            {
                "carrage-id": "10",
                "image": ["10-A.jpg", "10-B.jpg"],
                "score": [0.65, 0.35]
            },
            {
                "carrage-id": "11",
                "image": ["11-A.jpg", "11-B.jpg"],
                "score": [0.78, 0.22]
            },
            {
                "carrage-id": "12",
                "image": ["12-A.jpg", "12-B.jpg"],
                "score": [0.82, 0.18]
            }
        ]
    }
    return jsonify(mock_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) # Added host='0.0.0.0'
