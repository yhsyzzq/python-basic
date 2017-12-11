import socket

'''socket客户端'''

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999

clientSocket.connect((host, port))
print("客户端连接成功！\r\n")

message = clientSocket.recv(1024)
clientSocket.close()
print(message.decode('utf-8'))
