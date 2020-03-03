class Comment:
    def __init__(self, detail, view_times):
        self.detail = detail
        self.view_times = view_times

    def info(self):
        print('一条简单的评论，内容是%s' % self.detail)


c = Comment('疯狂Python讲义很不错', 20)
# 判断是否包含指定的属性或方法
print(hasattr(c, 'detail'))    # True
print(hasattr(c, 'view_times'))    # True
print(hasattr(c, 'info'))    # True
# 获取指定属性的属性值
print(getattr(c, 'detail'))    # '疯狂Python讲义很不错'
print(getattr(c, 'view_times'))    # 20
# 由于info是方法，故下面代码会提示：name 'info' is not defined
# print(getattr(c, info, '默认值'))
# 为指定属性设置属性值
setattr(c, 'detail', '天气不错')
setattr(c, 'view_times', 32)
# 输出重新设置后的属性值
print(c.detail)
print(c.view_times)