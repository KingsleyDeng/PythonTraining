import matplotlib.pyplot as plt
import random

plt.figure()
x_data, y_data = [], []
for i in range(5000):
    x_data.append(random.uniform(-3, 3))
for i in range(5000):
    y_data.append(random.uniform(-3, 3))
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.scatter(x_data,
            y_data,
            c='purple',
            s=50,
            alpha=0.5,
            marker='p',
            linewidths=1,
            edgecolors=['green', 'yellow'])
# 绘制第二个散点图（只包含一个起点），突出起点
plt.scatter(x_data[0], y_data[0], c='red', s=150, alpha=1)
# 绘制第三个散点图（只包含一个结束点），突出结束点
plt.scatter(x_data[4999], y_data[4999], c='black', s=150, alpha=1)
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.gca().spines['bottom'].set_position(('data', 0))
plt.gca().spines['left'].set_position(('data', 0))
plt.title('随机数的散点图')
plt.show()

