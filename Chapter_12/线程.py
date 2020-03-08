import threading


def action(max):
    for i in range(max):
        # 调用threading模块的current_thread()函数获取当前线程
        # 调用线程对象的getName()方法获取当前线程的名字
        print(threading.current_thread().getName() + " " + str(i))


# 下面是主程序
for i in range(100):
    print(threading.current_thread().getName() + " " + str(i))
    if i == 20:
        t1 = threading.Thread(target=action, args=(100,))
        t1.start()
        t2 = threading.Thread(target=action, args=(100,))
        t2.start()

print("主线程执行完成！")
