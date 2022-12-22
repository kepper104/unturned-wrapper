from flask import Flask, render_template, jsonify
from threading import Thread
from time import sleep


class ServerControl:
    def __init__(self):
        self.app = Flask(__name__)
        self.server_logs = ""

        @self.app.route("/")
        def index():
            with open("index.html", 'r') as f:
                index = f.read()
            return index

        @self.app.route("/start")
        def start_server():
            # Insert code here to start the server
            self.server_logs += "Starting server...\n"
            return jsonify({"logs": self.server_logs})

        @self.app.route("/stop")
        def stop_server():
            # Insert code here to stop the server
            self.server_logs += "Stopping server...\n"
            return jsonify({"logs": self.server_logs})

        @self.app.route("/restart")
        def restart_server():
            # Insert code here to restart the server
            self.server_logs += "Restarting server...\n"
            return jsonify({"logs": self.server_logs})

    def run(self):
        self.app.run(debug=False, host='0.0.0.0')
