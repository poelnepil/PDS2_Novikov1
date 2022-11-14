# '''client'''
import socket

sock = socket.socket()
sock.connect(('localhost', 8000))
inpt = str(input('input a sentence: '))
sock.send(inpt.encode())
data = sock.recv(1024).decode()
print(data)
sock.close()