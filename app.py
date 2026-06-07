import os
import requests
from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Core Configurations for GitHub
# This pulls the token dynamically from the ~/.bashrc variable we created earlier
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN") 

# TODO: Change these strings to match your real GitHub setup!
REPO_OWNER = "guvengucuyener"  # Your GitHub Username
REPO_NAME = "CICDPOC"          # Your GitHub Repository Name
WORKFLOW_FILE = "ansible-deploy.yml"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/commit', methods=['POST'])
def commit():
    if not GITHUB_TOKEN:
        return jsonify({"status": "error", "message": "System Error: GITHUB_TOKEN environment variable is missing on this server."}), 500

    ui_data = request.json  # Array of rows from the HTML table
    
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/actions/workflows/{WORKFLOW_FILE}/dispatches"
    
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    
    payload = {
        "ref": "main",
        "inputs": {
            # CRITICAL CHANGE HERE: Convert the Python dictionary/list to a strict JSON string!
            "network_data": json.dumps(ui_data)  
        }
    }
    
    response = requests.post(url, json=payload, headers=headers)
    print(f"GitHub API Response Status: {response.status_code}")
    
    if response.status_code == 204:
        return jsonify({"status": "success", "message": "Pipeline triggered successfully on GitHub!"}), 200
    else:
        return jsonify({"status": "error", "message": f"GitHub API Error: {response.text}"}), response.status_code
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
