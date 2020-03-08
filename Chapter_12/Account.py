import threading
import time


# 线程安全类的特征：
# 1.该类的对象可以被多个线程安全地访问
# 2.每个线程在调用该对象的任意方法之后，都将得到正确的结果
# 3.每个线程在调用该对象的任意方法之后，该对象都依然保持合理的状态

class Account:
    # 定义构造器
    def __init__(self, account_no, balance):
        # 封装账户编号和账户余额两个变量
        self.account_no = account_no
        self._balance = balance
        self.lock = threading.RLock()

    def getBalance(self):
        return self._balance

    def draw(self, draw_amount):
        #         加锁
        self.lock.acquire()
        try:
            # 账户余额大于取钱数目
            if self._balance >= draw_amount:
                # 吐出钞票
                print(threading.current_thread().name + "取钱成功！吐出钞票：" +
                      str(draw_amount))
                time.sleep(0.001)
                # 修改余额
                self._balance -= draw_amount
                print("\t余额为：" + str(self._balance))
            else:
                print(threading.current_thread().name + "取钱失败！余额不足！")
        finally:
            # 修改完成 解放锁
            self.lock.release()
