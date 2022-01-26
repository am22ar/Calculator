import socket
s = socket.socket()
host = socket.gethostname()
port = 5000
s.connect((host , port))
msg = input(' -> ')

while msg.lower().strip() != 'bye':
    s.send((msg.encode()))
    data = s.recv(1024).decode()
    print('received from server:--  ' + data)
    msg = input(' -> ')

s.close()