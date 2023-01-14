import cv2
import socket
import pickle

# 创建一个socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定socket到特定地址和端口
server_socket.bind(('0.0.0.0', Server_Port))

# 开始监听客户端连接
server_socket.listen(5)

while True:
    # 接受客户端的连接
    client_socket, addr = server_socket.accept()

    while True:
        # 接收图像的大小
        size = int(client_socket.recv(1024).decode())

        # 接收图像数据
        data = b''
        while len(data) < size:
            data += client_socket.recv(1024)

        # 解码图像数据
        frame = pickle.loads(data)

        # 显示图像
        cv2.imshow("来自客户端的图像", frame)
        cv2.waitKey(1)

# 关闭服务器socket
server_socket.close()
