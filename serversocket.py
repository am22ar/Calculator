import socket

s=socket.socket()
print("socket created")

host = socket.gethostname()
port=12345

s.bind((host , port))
print("socket binded to %s" %port)

s.listen(3)

print("socket is listening")

while True:
    c, addr=s.accept()
    print("got connection from", addr)
    c.send("heelllooo everyone".encode())
    c.close()
    break


