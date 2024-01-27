from flask import Flask, request, jsonify
import socket
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_ip():
    # Return the private IP address of the EC2 instance
    hostname = socket.gethostname()
    private_ip = socket.gethostbyname(hostname)
    return private_ip

@app.route('/', methods=['POST'])
def handle_post():
    # Trigger the CPU stress test in a separate process
    subprocess.Popen(["python3", "stress_cpu.py"])
    return jsonify(success=True), 200

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)
