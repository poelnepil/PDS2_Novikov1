# '''client'''
import socket

sock = socket.socket()

name = input('enter a name: ')
sock.connect(('localhost', 8000))
sock.send(name.encode())
server = sock.recv(1024)
server = server.decode()
print(server, 'connected')

while True:
    message = input('me: ')
    sock.send(message.encode())
    message = sock.recv(1024)
    message = message.decode()
    print(server, ':', message)