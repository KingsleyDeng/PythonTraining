import threading


class FKThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.i = 0

    # 重写run方法作为线程执行体
    def run(self):
        while self.i < 100:
            # 调用threading模块中的current_thread()函数获取当前线程
            # 调用线程对象的getName()方法获取当前线程的名字
            print(threading.current_thread().getName() + " " + str(self.i))
            self.i += 1


for i in range(100):
    print(threading.current_thread().getName() + " " + str(i))
    if i == 20:
        ft1 = FKThread()
        ft1.start()
        ft2 = FKThread()
        ft2.start()
print("主线程执行完成")
