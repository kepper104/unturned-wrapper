import subprocess

# Start the process and store the Popen object
popen = subprocess.Popen(["./UnturnedHelper.sh"], stdout=subprocess.PIPE,
                         stdin=subprocess.PIPE, universal_newlines=True)

# Iterate over the output of the process
for stdout_line in iter(popen.stdout.readline, ""):
    print(stdout_line, end="")


def send_input(input_str):
    # Send input to the process
    popen.stdin.write(input_str)
    popen.stdin.flush()


# Example usage
send_input("input string\n")

# Close the stdout stream and wait for the process to finish
popen.stdout.close()
return_code = popen.wait()
if return_code:
    raise SystemError
