class Poker:
    # 定义构造方法
    def __init__(self):
        self.flowers = ('♠', '♥', '♣', '♦')
        self.values = ('2', '3', '4', '5', '6', '7', '8', '9'
                       '10', 'J', 'Q', 'K', 'A')
        self.__changed = {}
        self.__deleted = []

    # 定义__len__方法，返回序列长度
    def __len__(self):
        return 52

    # 定义__getitem__方法，用于获取序列中位置为key的元素
    def __getitem__(self, key):
        # 判断key是否合法
        check_key(key)
        # 如果在__changed中找到已经修改后的数据，则返回该数据
        if key in self.__changed:
            return self.__changed[key]
        # 如果在__deleted中找到已经删除的数据，则返回None
        if key in self.__deleted:
            return None
        # 否则根据计算返回序列值
        flower = key // 13
        value = key % 13
        return self.flowers[flower] + self.values[value]

    # 定义__setitem__方法，修改序列值
    def __setitem__(self, key, value):
        # 判断key是否合法
        check_key(key)
        # 将序列位置为key的元素值设置为value
        self.__changed[key] = value

    # 定义__delitem__方法，用于删除序列中的值
    def __delitem__(self, key):
        # 判断key是否合法
        check_key(key)
        # 如果要删除的元素没有包含在__deleted中，则添加
        if key not in self.__deleted:
            self.__deleted.append(key)
        # 如果要删除的元素包含在__changed中，则删除
        if key in self.__changed:
            del self.__changed[key]


def check_key(key):
    # 如果key不是整数，则抛出TypeError异常
    if not isinstance(key, int):
        raise TypeError('索引值必须是整数')
    # 如果key大于52，则抛出IndexError异常
    if key >= 52 or key < 0:
        raise IndexError('索引值必须在0~52之间')


if __name__ == '__main__':
    cq = Poker()
    print(len(cq))
    print(cq[2])    # '♠4'
    print(cq[1])    # '♠3'
    # 修改cq[1]元素
    cq[1] = '♣2'
    # 打印修改之后的cq[1]
    print(cq[1])    # '♣2'
    # 删除cq[1]
    del cq[1]
    print(cq[1])    # None
    # 再次对cq[1]赋值
    cq[1] = '♦5'
    print(cq[1])    # ♦5
    for pk in cq:
        print(pk)