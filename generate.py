#!/bin/env python
import socket
import sys


def help():
    print "Usage: ./generate.py [lists/textfile.txt]"


def dnsresolve(data):
    try:
        result = socket.gethostbyname_ex(data)
        return result[2]
    except KeyboardInterrupt:
        sys.exit(1)  # User escape with Ctrl + C
    except:
        return ["Failed to resolve " + data]

if len(sys.argv) < 2:
    help()  # Show Usage
else:
    f = open('lists/witopia.txt', 'r')
    for line in f:
        for item in dnsresolve(line.strip()):
            print item
    f.close()
