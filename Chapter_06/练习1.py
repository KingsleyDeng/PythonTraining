class Student:

    def __init__(self, name, age, gender, phone, address, email):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.address = address
        self.email = email

    # 定义方法吃
    def eat(self):
        print('%s正在吃东西。' % self.name)

    # 定义喝方法
    def drink(self):
        print('%s正在喝东西' % self.name)

    # 定义玩方法
    def play(self):
        print('%s正在玩！' % self.name)

    # 定义睡方法
    def sleep(self):
        print('%s睡觉了！' % self.name)

def find_for_name(student_lst, name):
    result = []
    for student in student_lst:
        if student.name == name:
            result.append(student)
    if result:
        print('找到姓名为%s的学生%d个' % (name, len(result)))
    else:
        print('没有找到姓名为%s的学生' % name)


def find_for_email(student_lst, email):
    result = []
    for student in student_lst:
        if student.email == email:
            result.append(student)
    if result:
        print('找到邮箱为%s的学生%d个' % (email, len(result)))
    else:
        print('没有找到邮箱为%s的学生' % email)


def find_for_address(student_lst, address):
    result = []
    for student in student_lst:
        if student.address == address:
            result.append(student)
    if result:
        print('找到邮箱为%s的学生%d个' % (address, len(result)))
    else:
        print('没有找到邮箱为%s的学生' % address)


s1 = Student(
    '张三',
    20,
    '男',
    '13312345678',
    '中国·重庆市渝北区二支路街道180号',
    'zhangsan@163.com')
s2 = Student(
    '李四',
    21,
    '男',
    '13312348970',
    '中国·重庆市渝北区二支路街道181号',
    'lisi@163.com')
s3 = Student(
    '王麻子',
    33,
    '男',
    '13312343456',
    '中国·重庆市渝北区二支路街道182号',
    'wangmazi@163.com')
student_lst = [s1, s2, s3]
find_for_name(student_lst, '张三')
find_for_name(student_lst, '王二小')
find_for_email(student_lst, 'lisi@163.com')
find_for_email(student_lst, 'xxx@xxx.com')
find_for_address(student_lst, '中国·重庆市渝北区二支路街道182号')
find_for_address(student_lst, '中国·重庆市渝北区二支路街道183号')


if __name__ == '__main__':
    s = Student('张三', 20, '男', '13312345678', '中国·重庆市渝北区二支路街道180号', 'zhangsan@163.com')
    print('姓名：%s，年龄：%d，性别：%s，电话号码：%s，地址：%s，邮箱：%s' % (
        s.name, s.age, s.gender, s.phone, s.address, s.email
    ))

    s.eat()
    s.drink()
    s.play()
    s.sleep()
