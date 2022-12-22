from flask import Flask, render_template, jsonify
from threading import Thread
from time import sleep
from os import chdir


class ServerControl:
    def __init__(self):
        self.app = Flask(__name__)
        self.server_logs = ""
        # self.index_path = "/home/kepper104/hosting/unturned-wrapper/index.html"
        chdir("/home/kepper104/hosting/unturned-wrapper/")
        self.index_path = "index.html"
        # self.index_path = ''
        # with open("index.html", 'r') as f:
        #     self.index_path = f.read()

        @self.app.route("/")
        def index():
            # self.server_logs += "hell o\n"
            return render_template(self.index_path, logs=self.server_logs)

        @self.app.route("/start")
        def start_server():
            print("START SERVER")
            self.server_logs += "Starting server...\n"
            return render_template(self.index_path, logs=self.server_logs)

        @self.app.route("/stop")
        def stop_server():
            print("STOP SERVER")
            self.server_logs += "Stopping server...\n"
            return render_template(self.index_path, logs=self.server_logs)

        @self.app.route("/restart")
        def restart_server():
            print("RESTART SERVER")
            self.server_logs += "Restarting server...\n"
            return render_template(self.index_path , logs=self.server_logs)

    def run(self):
        self.app.run(debug=False, host='0.0.0.0')

