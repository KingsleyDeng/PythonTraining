class Vehicle:
    # 定义构造方法
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed


class Car(Vehicle):
    # 定义构造方法
    def __init__(self, name, speed):
        super().__init__(name, speed)


class Train(Vehicle):
    # 定义构造方法
    def __init__(self, name, speed):
        super().__init__(name, speed)


class Airplane(Vehicle):
    # 定义构造方法
    def __init__(self, name, speed):
        super().__init__(name, speed)