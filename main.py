#!/usr/bin/env python
import os
import pty
import sys

with open('log', 'ab') as file:
    def read(fd):
        data = os.read(fd, 1024)
        file.write(data)
        file.flush()
        return data

    pty.spawn([sys.executable, "test.py"], read)