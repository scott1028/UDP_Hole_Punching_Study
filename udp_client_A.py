# coding: utf-8
# UDP Hole Punching Testing - Symmetric Nat Side

import time
import socket

UDP_IP = "XX.XX.XX.XX"  # ${server_B_ip}
UDP_PORT = 5005  # 兩邊相同即可
MESSAGE = "Hello, World!"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

while True:
	sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
	print "send message:", MESSAGE
	time.sleep(2)
