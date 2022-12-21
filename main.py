import pexpect
program = pexpect.spawn("python3 test.py")
program.expect('Name')

print(program.before.decode())
program.interact()

