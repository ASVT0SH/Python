"""TCP Client Example"""
import socket
import sys

host = "localhost"
port = 50000
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.send("Hello, world".tcpsocket)
data = s.recv(size)
s.close()
print("Received:", data)
