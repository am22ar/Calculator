import  socket
s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
print("successfully created socket")

port = 80
host_ip = socket.gethostbyname('www.yahoo.com')


s.connect((host_ip , port))
print("socket has connected to yahoooooo")
