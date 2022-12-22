from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, emit
from threading import Thread
from time import sleep
from os import chdir


class ServerControl:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['SECRET_KEY'] = 'secret!'
        socketio = SocketIO(self.app)
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

        @socketio.on('start')
        def start_server():
            # Insert code here to start the server
            self.server_logs += "Starting server...\n"
            emit('update', {'logs': self.server_logs}, broadcast=True)

        @socketio.on('stop')
        def stop_server():
            # Insert code here to stop the server
            self.server_logs += "Stopping server...\n"
            emit('update', {'logs': self.server_logs}, broadcast=True)

        @socketio.on('restart')
        def restart_server():
            # Insert code here to restart the server
            self.server_logs += "Restarting server...\n"
            emit('update', {'logs': self.server_logs}, broadcast=True)

    def run(self):
        self.app.run(debug=False, host='0.0.0.0')

