import socket
import threading
import utility.json_reader as jr

path = '../assets/gptConfig.json'


def send_message(message='', ip=None, port=None):
    # 检测服务器是否在运行
    if threading.active_count() >= 2:
        pass
    else:
        print("开始发送信息")
        # 是否从配置文件中读取数据，其中ip需要是字符串，port需要是整型
        reader = jr.JsonReader(file_path=path, instance_name='netConfig')
        ip = ip or reader.get_property('ip')
        port = port or int(reader.get_property('port'))
        # 创建新的线程用以发送信息
        thread = SocketThread(thread_id=1, thread_name=str("socket"), sleep_time=0.5, message=message,
                              ip=ip,
                              port=port
                              )
        thread.start()


# 小括号中的：threading.Thread，意味着这个类继承自threading.Thread类
class SocketThread(threading.Thread):
    def __init__(self, thread_id, thread_name, sleep_time, message, ip, port):
        super().__init__()
        self.thread_id = thread_id
        self.thread_name = thread_name
        self.sleep_time = sleep_time
        self.message = message
        self.ip = ip
        self.port = port

    def run(self):
        # 使用with语句协助管理内存
        with socket.socket() as server:
            # 其实这个server可以放至send_message函数中创建，就不需要再反复创建，不过现在暂不修改。
            server.bind((self.ip, self.port))
            server.listen(1)
            client, addr = server.accept()
            # 发送信息
            client.send(self.message.encode('utf-8'))
            # 释放资源，有with语句在，这两句不写也没问题
            client.close()
            server.close()
        print("线程退出:", self.thread_name)
