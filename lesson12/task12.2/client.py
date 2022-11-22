import socket

sock = socket.socket()
sock.connect(('localhost', 55000))
a = input('number1:')
b = input('number2:')
r = f'{a} {b}'
sock.send(str(r).encode())
data = sock.recv(1024).decode()
print(data)
sock.close()
