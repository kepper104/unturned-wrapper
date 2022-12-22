import pexpect
from os import chdir

chdir('/home/kepper104/hosting/unturned/')
c = pexpect.spawn('./ServerHelper.sh')
c.expect("unused Assets to reduce memory usage")

c.sendline("players")
c.expect("any players.")
print(c.read())