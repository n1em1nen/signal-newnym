#!/usr/bin/env python
import sys
import telnetlib
import socks
import socket
 
HOST = "127.0.0.1"
password = ""
tn = telnetlib.Telnet(HOST, 9051)
 
tn.write('AUTHENTICATE "' + password + '"\n')
 
tn.read_until("250 OK")
tn.write('signal newnym\n')
tn.read_until("250 OK")
tn.write("quit\n")
tn.read_until("250 closing connection")

def create_connection(address, timeout=None, source_address=None):
    sock = socks.socksocket()
    sock.connect(address)
    return sock

socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)

# patch the socket module
socket.socket = socks.socksocket
socket.create_connection = create_connection

import urllib2
f = urllib2.urlopen('http://icanhazip.com')
print f.read()
