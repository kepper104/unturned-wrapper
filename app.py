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



    def run(self):
        self.app = Flask(__name__)
        self.turbo = Turbo(self.app)
        # self.app.config['SECRET_KEY'] = 'secret!'
        self.server = Interactor(self)
        t = Thread(target=self.server.start, args=())
        t.start()
        # print("STARTED " * 1000)
        # self.start_server()

        @self.app.route("/")
        def index():
            # self.server_logs += "hell o\n"
            return render_template(self.index_path)

        @self.app.route("/start_server")
        def start_server():
            print("HI")
            # Insert code here to start the server
            self.server_logs += "Starting server...\n"
            # emit('update', {'logs': self.server_logs}, broadcast=True)
            return "nothing"


        @self.app.context_processor
        def inject_load():
            return {'logs': self.server_logs[-50:]}

        @self.app.before_first_request
        def before_first_request():
            print("START THREAD\n" * 100)
            Thread(target=self.update_load).start()

        self.app.run(debug=False, host='0.0.0.0')

    def update_load(self):
        with self.app.app_context():
            while True:
                sleep(0.3)
                print("updating.....")
                self.turbo.push(self.turbo.replace(render_template('logs.html'), 'load'))

