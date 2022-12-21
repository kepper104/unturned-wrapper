import subprocess

class Interactor():

    # Start the process and store the Popen object
    def __init__(self):
        self.popen = subprocess.Popen(["./ServerHelper.sh"], stdout=subprocess.PIPE,
                                 stdin=subprocess.PIPE, universal_newlines=True)

        # Iterate over the output of the process
        for stdout_line in iter(self.popen.stdout.readline, ""):
            print(stdout_line, end="")

        self.popen.stdout.close()
        return_code = self.popen.wait()
        if return_code:
            raise SystemError


    def send_input(self, input_str):
        # Send input to the process
        self.popen.stdin.write(input_str)
        self.popen.stdin.flush()


    # Example usage
    # send_input("input string\n")

# Close the stdout stream and wait for the process to finish

i = Interactor()
