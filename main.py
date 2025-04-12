from flask import Flask, request, jsonify, send_file
import subprocess
import os
import signal
import webfiles

app = Flask(__name__)

# Define the path to the Python script you want to run and stop
path = None
pid = None

# Function to start the Python script
def start_script():
    global pid 
    if(path is not None):
        pid = subprocess.Popen(["sudo", "python3", path]).pid

# Function to stop the Python script
def stop_script():
    global pid
    if pid is not None:
        try:
            # Send SIGTERM to the process
            os.kill(pid, signal.SIGTERM)
        except OSError as e:
            print(f"Error stopping script: {e}")
        finally:
            # Reset pid to None after stopping
            pid = None
    subprocess.Popen(["sudo", "python3", "user/clear.py"])

@app.route('/')
def index():
    """ This function creates the html code for a website which lets the user enter a password. """
    return webfiles.login_page()

@app.route('/programs', methods=['POST'])
def home_action():
    data = request.form
    print(data)
    action = data.get('action')
    uname = data.get('uname')
    if uname is None:
        uname = 'default'
    print(action)
    if action == 'start':
        stop_script()
        global path
        path = data.get('program')
        if path is None:
            return jsonify({'error': 'No program specified'}), 400
        path = os.path.join('./user/'+uname, path)
        start_script()
        #return jsonify({'status': 'Script started'}), 200
    elif action == 'stop':
        stop_script()
        #return jsonify({'status': 'Script stopped'}), 200
    elif action == 'delete':
        program = data.get('program')
        if program is None:
            return jsonify({'error': 'No program specified'}), 400
        file_path = os.path.join('./user/'+uname, program)
        try:
            os.remove(file_path)
            #return jsonify({'status': 'File deleted successfully'}), 200
        except FileNotFoundError:
            return jsonify({'error': 'File not found'}), 404
    elif action == 'upload':
        if 'file' not in request.files:
            return jsonify({'error': 'No file part in the request'}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        if file:
            upload_folder = os.path.join('./user', uname)
            os.makedirs(upload_folder, exist_ok=True)
            file_path = os.path.join(upload_folder, file.filename)
            file.save(file_path)
    elif action == 'lib_upload':
        if 'file' not in request.files:
            return jsonify({'error': 'No file part in the request'}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        if file:
            upload_folder = os.path.join('./user', uname)
            upload_folder = os.path.join(upload_folder, "lib")
            os.makedirs(upload_folder, exist_ok=True)
            file_path = os.path.join(upload_folder, file.filename)
            file.save(file_path)
    elif action == 'download':
        program = data.get('program')
        if program is None:
            return jsonify({'error': 'No program specified'}), 400
        file_path = os.path.join('./user/'+uname, program)
        if os.path.exists(file_path):
            return send_file(file_path, as_attachment=True)
        else:
            return jsonify({'error': 'File not found'}), 404
    return webfiles.program_page(uname)

@app.route('/programs', methods=['GET'])
def home():
    uname = request.args.get('uname')
    if uname is None:
        uname = 'default'
    return webfiles.program_page(uname)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="80", debug=True, use_reloader=False)
