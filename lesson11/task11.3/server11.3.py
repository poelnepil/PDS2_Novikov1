# ''' server '''
import socket
sock = socket.socket()
sock.bind(('', 8000))
sock.listen()
while True:
    conn, addr = sock.accept()
    print('connected:', addr)
    data1 = conn.recv(1024).decode()
    print(data1)
    data1 = data1.split()
    data2 = ''.join(data1)
    data = len(data2)
    conn.send(str(data).encode())
    conn.close()