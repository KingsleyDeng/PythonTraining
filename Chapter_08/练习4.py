def poker_generator():
    nums = 52
    flowers = ('♠', '❤', '♣', '♦')
    values = ('2', '3', '4', '5', '6', '7', '8', '9',
              '10', 'J', 'Q', 'K', 'A')
    for i in range(nums):
        yield flowers[i // 13] + values[i % 13]


if __name__ == '__main__':
    pk = poker_generator()
    print(next(pk))    # ♠2，生成器“冻结”在yield处
    print(next(pk))    # ♠3，生成器再次冻结在yield处
    for el in pk:
        print(el, end=' ')