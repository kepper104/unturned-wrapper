import pexpect
from os import chdir
from app import ServerControl
from threading import Thread

# commands = {"players": ["any players."],
#             "admins": [""]}


class Interactor:
    def __init__(self, flask_app):

        self.flask_app = flask_app
        print("Started Controller")
        chdir("/home/kepper104/hosting/unturned/")
        self.child = pexpect.spawn("./ServerHelper.sh")
        self.child.timeout = 99999999
        self.started = False
        self.command = None
        print("Beginning reading...")
        self.read()


    def read(self):
        for line in self.child:
            self.flask_app.server_logs += line.decode()
            print(line.decode())
            if "Loading level: 100%" in line.decode():
                self.started = True
            if self.command:
                print("command searching...")
            # if "CreateObjectMapping:" in line.decode() and self.started:
            #     print("FOUND " * 10)
            #     self.child.sendline("players")
            #     print("SENT PLAYERS")
