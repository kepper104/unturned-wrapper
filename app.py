from flask import Flask, render_template, jsonify
from threading import Thread
from time import sleep
from os import chdir
from expect import Interactor
from turbo_flask import Turbo

class ServerControl:
    def __init__(self):

        self.server_logs = ""
        # self.index_path = "/home/kepper104/hosting/unturned-wrapper/index.html"
        chdir("/home/kepper104/hosting/unturned-wrapper/")
        self.index_path = "index.html"
        # self.index_path = ''
        # with open("index.html", 'r') as f:
        #     self.index_path = f.read()



        # @socketio.on('stop')
        # def stop_server():
        #     # Insert code here to stop the server
        #     self.server_logs += "Stopping server...\n"
        #     emit('update', {'logs': self.server_logs}, broadcast=True)
        #
        # @socketio.on('restart')
        # def restart_server():
        #     # Insert code here to restart the server
        #     self.server_logs += "Restarting server...\n"
        #     emit('update', {'logs': self.server_logs}, broadcast=True)

    def run(self):
        self.app = Flask(__name__)
        self.app.config['SECRET_KEY'] = 'secret!'
        self.start_server()

        @self.app.route("/")
        def index():
            # self.server_logs += "hell o\n"
            return render_template(self.index_path, logs=self.server_logs)

        @self.app.route("/start_server")
        def start_server():
            print("HI")
            # Insert code here to start the server
            self.server_logs += "Starting server...\n"
            # emit('update', {'logs': self.server_logs}, broadcast=True)
        self.app.run(debug=False, host='0.0.0.0')


    def start_server(self):
        self.server = Interactor(self)
        t = Thread(target=self.server.start())
        t.start()

