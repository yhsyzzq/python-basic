import socket

'''socket服务端'''

# 创建 socket 对象
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本机主机名
host = socket.gethostname()

# 设置监听端口号
port = 9999

# 绑定主机名和端口号
serverSocket.bind((host, port))
# 设置最大连接数为5
serverSocket.listen(5)

while True:
    print("服务端启动成功！")
    clientSocket, address = serverSocket.accept()
    print("连接地址：%s" % str(address))

    message = "欢迎访问服务端！\r\n"
    clientSocket.send(message.encode("utf-8"))
    clientSocket.close()
