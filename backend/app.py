from flask import Flask, jsonify
from flask_cors import CORS # Import CORS

app = Flask(__name__)
CORS(app) # Enable CORS for all routes

@app.route('/<taskid>')
def get_task_details(taskid):
    # Mock data for now, as per TASK.md
    mock_data = {
        "taskID": taskid,
        "car-id": "2640",
        "begintime": 1702060386,
        "endtime": 1702060386,
        "carrages": 12,
        "details": [
            {
                "carrage-id": "01",
                "image": ["1.bmp", "2.bmp"],
                "score": [0.8, 0.2]
            },
            {
                "carrage-id": "02",
                "image": ["3.bmp", "4.bmp"],
                "score": [0.8, 0.2]
            },
            {
                "carrage-id": "03",
                "image": ["5.bmp", "6.bmp"],
                "score": [0.7, 0.3]
            },
            {
                "carrage-id": "04",
                "image": ["7.bmp", "8.bmp"],
                "score": [0.9, 0.1]
            },
            {
                "carrage-id": "05",
                "image": ["9.bmp", "10.bmp"],
                "score": [0.6, 0.4]
            },
            {
                "carrage-id": "06",
                "image": ["11.bmp", "12.bmp"],
                "score": [0.5, 0.5]
            }
        ]
    }
    return jsonify(mock_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) # Added host='0.0.0.0'
