# ''' server '''
import socket

sock = socket.socket()
sock.bind(('', 8000))
sock.listen()

print('server is working')
name = 'server'
conn, addr = sock.accept()
client = conn.recv(1024).decode()
print(client, 'connected')
conn.send(name.encode())

while True:
    message = input('my server: ')
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(client, ':', message)