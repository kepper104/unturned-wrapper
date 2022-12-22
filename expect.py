import pexpect
from os import chdir

commands = {"players": ["any players."],
            "admins": [""]}
class Interactor():
    def __init__(self):

        chdir("/home/kepper104/hosting/unturned/")
        self.child = pexpect.spawn("./ServerHelper.sh")
        self.started = False
        self.command = None
        self.read()

    def read(self):
        for line in self.child:
            print(line.decode())
            if "Loading level: 100%" in line.decode():
                self.started = True
            if self.command:
                print("command searching...")
            if "CreateObjectMapping:" in line.decode() and self.started:
                print("FOUND " * 10)
                self.child.sendline("players")
                print("SENT PLAYERS")

#print(c.read())
interactor = Interactor()