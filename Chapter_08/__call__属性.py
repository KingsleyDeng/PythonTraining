class User:
    def __init__(self, name, passwd):
        self.name = name
        self.passwd = passwd

    def validLogin(self):
        print('验证%s登陆' % self.name)


u = User('crazyit', 'leegang')
# 判断u.name是否包含__call__方法
print(hasattr(u.name, '__call__'))    # False
# 判断u.passwd是否包含__call__方法
print(hasattr(u.passwd, '__call__'))    # False
# 判断u.validLogin是否包含__call__方法
print(hasattr(u.validLogin, '__call__'))    # True