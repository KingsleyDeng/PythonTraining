import threading
import Account


# 定义一个函数来模拟取钱操作
def draw(account, draw_amount):
    account.draw(draw_amount)


# 创建账户
acct = Account.Account("1234566", 1000)

threading.Thread(name='甲', target=draw, args=(acct, 800)).start()
threading.Thread(name='乙', target=draw, args=(acct, 800)).start()
