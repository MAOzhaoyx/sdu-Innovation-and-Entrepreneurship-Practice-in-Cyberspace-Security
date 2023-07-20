import socket
import time

# 定义服务器地址和端口号
SERVER_ADDRESS = ('192.168.206.1', 8000)

# 创建套接字对象
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接服务器
sock.connect(SERVER_ADDRESS)


# 自定义协议方法，用于发送消息并接收响应
def send_receive_message(message):
    # 发送消息给服务器
    sock.sendall(message.encode())

    # 接收服务器的响应
    response = sock.recv(1024).decode()

    return response



def calculate_run_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        run_time = end_time - start_time
        print(f"代码运行时间：{run_time} 秒")
        return result

    return wrapper


@calculate_run_time
def main():
    # 示例消息
    message = "Hello World!"

    # 发送消息并接收响应
    response = send_receive_message(message)

    # 打印响应
    print(f"服务器响应：{response}")


if __name__ == "__main__":
    main()
