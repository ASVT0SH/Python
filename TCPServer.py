"""TCP Server Example"""
import socket
import sys

host = "localhost"
port = 50000
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
while 1:
    client, address = s.accept()
    data = client.recv(size)
    if data:
        client.send(data)
        client.close()
print("Received:", data)
print("Connection from:", address)
print("Sending: ", data)
client.send(data)
client.close()
