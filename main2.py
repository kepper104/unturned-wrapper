import subprocess
import os
class Interactor():

    # Start the process and store the Popen object
    def __init__(self):
        print('inited')
    async def start(self):
        print("START " * 100)
        # os.chdir("/home/kepper104/steamcmd/unturned/")
        os.chdir("/home/kepper104/hosting/unturned")
        self.popen = subprocess.Popen(["./ServerHelper.sh"], stdout=subprocess.PIPE,
                                 stdin=subprocess.PIPE, universal_newlines=True)

        # Iterate over the output of the process
        for stdout_line in iter(self.popen.stdout.readline, ""):
            print(stdout_line, end="")

        self.popen.stdout.close()
        return_code = self.popen.wait()
        if return_code:
            raise SystemError


    async def send_input(self, input_str):
        # Send input to the process
        print(input_str * 100)
        self.popen.stdin.write(input_str)
        self.popen.stdin.flush()


    # Example usage
    # send_input("input string\n")

# Close the stdout stream and wait for the process to finish
#
# i = Interactor()

import time

#
# class Interactor():
#     def __init__(self):
#         print("initiated")
#         # print("start")
#         # # print("con")
#         # time.sleep(3)
#         # print("3 secs past")
#     async def send(self):
#         print("sent from self")
#     async def start(self):
#         i = 10
#         while True:
#             i += 1
#             # print("i", end='')