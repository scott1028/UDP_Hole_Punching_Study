# coding: utf-8
# UDP Hole Punching Testing - Full Cone Nat Side

import time
import socket

UDP_IP = "0.0.0.0"
UDP_PORT = 5005  # 兩邊相同即可

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    sock.send('Server say hi!', addr)
    print "received message:", data
    time.sleep(2)
