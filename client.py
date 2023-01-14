import cv2
import socket
import pickle

# 初始化摄像头
cap = cv2.VideoCapture(0)

# 创建一个socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接到服务器
client_socket.connect(('Server_IP', Server_Port))

while True:
    # 从摄像头捕获图像
    ret, frame = cap.read()

    # 将图像编码为jpeg
    data = pickle.dumps(frame)
    size = len(data)

    # 发送图像的大小
    client_socket.sendall(str(size).encode())

    # 发送图像
    client_socket.sendall(data)

# 释放摄像头和关闭socket
cap.release()
client_socket.close()
