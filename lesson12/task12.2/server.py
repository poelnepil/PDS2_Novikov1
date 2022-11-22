import asyncio
import socket

async def handle_client(client):
    loop = asyncio.get_event_loop()
    request = None
    while True:
        request = (await loop.sock_recv(client, 1024)).decode('utf8')
        global s
        s = request.split(' ')
        await plus()
        await minus()
        await multy()
        answer = f'number1+number2={res1};\nnumber1-number2={res2};\nnumber1*number2={res3}'
        await loop.sock_sendall(client, answer.encode())
        break
    client.close()


async def plus():
    global res1
    res1 = int(s[0]) + int(s[1])
    await asyncio.sleep(1)
    print(f'number1+number2={res1}')

async def minus():
    global res2
    res2 = int(s[0]) - int(s[1])
    await asyncio.sleep(1)
    print(f'number1-number2={res2}')

async def multy():
    global res3
    res3 = int(s[0]) * int(s[1])
    await asyncio.sleep(1)
    print(f'number1*number2={res3}')


async def run_server():
    server = socket.socket()
    print('connected:', server)
    print('server alive')
    server.bind(('localhost', 55000))
    server.listen(8)
    server.setblocking(False)
    loop = asyncio.get_event_loop()
    while True:
        client, _ = await loop.sock_accept(server)
        loop.create_task(handle_client(client))

asyncio.run(run_server())