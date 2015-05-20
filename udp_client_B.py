# coding: utf-8
# UDP Hole Punching Testing - Symmetric Nat Side

import time
import socket

UDP_IP = "XX.XX.XX.XX"  # ${server_A_ip}
UDP_PORT = 44555  # Client-A 發出封包所使用的 src port

MESSAGE = "Another Server Client say Hello!"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind(('0.0.0.0', 5005))

while True:
	sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
	print MESSAGE
	time.sleep(1)
	data, addr = sock.recvfrom(1024)
	print "received message:", data
	time.sleep(1)
