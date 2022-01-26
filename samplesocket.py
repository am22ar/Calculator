import socket

s = socket.socket()

host = socket.gethostname()

port = 12345

#host='localhost'

s.connect((host , port))

print(s.recv(1024).decode())

s.close()


