import socket
s = socket.socket()
host = socket.gethostname()
port = 5000
s.bind((host , port))

s.listen(5)

conn, addr = s.accept()

print('connection from: ' + str(addr))

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print('from connected user:-- ' + str(data))
    data = input(' -> ')
    conn.send(data.encode())

conn.close()