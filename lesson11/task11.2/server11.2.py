# ''' server '''
import socket

sock = socket.socket()
sock.bind(('localhost', 8000))
sock.listen()

print('server is working')
name = 'server'
conn, addr = sock.accept()
client = conn.recv(1024).decode()
print(client, 'connected')
conn.send(name.encode())

while True:
    message = ['hi', 'everything is fine', 'i listen..', 'bye!']
    messagecl = conn.recv(1024)
    messagecl = messagecl.decode()
    print(client, ':', messagecl)
    if messagecl == 'hello' or messagecl == 'hi':
        conn.send(message[0].encode())
    elif messagecl == 'how are you?' or messagecl == 'whats up?':
        conn.send(message[1].encode())
    elif messagecl == 'goodbye':
        conn.send(message[-1].encode())
    else:
        conn.send(message[2].encode())