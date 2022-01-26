import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Socket successfully created")

port = 80

host_ip = socket.gethostbyname('www.yahoo.com')

s.connect((host_ip, port))

print("the socket has successfully connected to yahoo")
