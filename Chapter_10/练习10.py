
def fibonacci(n):
    result_lst = [1, 1]
    [result_lst.append(result_lst[-1] + result_lst[-2]) for i in range(2, n)]
    return result_lst


print(fibonacci(10))
# 计算fibonacci数列的元素的平方值
result = map(lambda x: x * x, fibonacci(10))
print([e for e in result], end=' ')