
from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/trigger_windsurf', methods=['POST'])
def trigger_windsurf():
    subprocess.Popen(['python3', 'scripts/windsurf_trigger.py'])
    return jsonify({'status': 'Windsurf triggered'})

@app.route('/trigger_builder', methods=['POST'])
def trigger_builder():
    subprocess.Popen(['python3', 'scripts/builder_trigger.py'])
    return jsonify({'status': 'Builder.io triggered'})

@app.route('/trigger_cursor', methods=['POST'])
def trigger_cursor():
    subprocess.Popen(['bash', 'scripts/cursor_trigger.sh'])
    return jsonify({'status': 'Cursor triggered'})

@app.route('/trigger_pipeline', methods=['POST'])
def trigger_pipeline():
    subprocess.Popen(['python3', 'scripts/azure_pipeline_trigger.py'])
    return jsonify({'status': 'Azure Pipeline triggered'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
