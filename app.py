import os
import requests
import json
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

GITLAB_URL = "https://gitlab.com" 
PROJECT_ID = "82944819" 
PERSONAL_ACCESS_TOKEN = "glpat-zRXMkypociXWXU7khBiZtWM6MQpvOjEKdTpuNXQ2YQ8.01.170mtdv3o"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/commit', methods=['POST'])
def commit():
    ui_data = request.json  # Raw data from the HTML table
    
    # 1. SAVE THE DATA LOCALLY ON THE SERVER INSTEAD OF SENDING TO GITLAB
    # We save it to a shared temp directory on your machine
    local_file_path = "/tmp/ui_input.json"
    with open(local_file_path, "w") as f:
        json.dump(ui_data, f)
        
    # 2. TRIGGER THE GITLAB PIPELINE CLEANLY (NO VARIABLES = NO SECURITY ERROR)
    url = f"{GITLAB_URL}/api/v4/projects/{PROJECT_ID}/pipeline"
    headers = {
        "PRIVATE-TOKEN": PERSONAL_ACCESS_TOKEN
    }
    payload = {
        "ref": "main"  # No "variables" block here anymore!
    }
    
    response = requests.post(url, json=payload, headers=headers)
    print(f"GitLab API Response: {response.status_code} - {response.text}")
    
    if response.status_code == 201:
        return jsonify({"status": "success", "message": "Pipeline started successfully!"}), 200
    else:
        return jsonify({"status": "error", "message": f"GitLab Error: {response.text}"}), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
