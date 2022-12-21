import pexpect
from os import chdir

chdir('/home/kepper104/hosting/unturned/')
c = pexpect.spawn('./ServerHelper.sh')
c.expect("ms)")
c.sendline("players")

print(c.before)