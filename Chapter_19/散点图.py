import matplotlib.pyplot as plt
import numpy as np

plt.figure()
# 定义从-pi到pi之间的数据，平均取64个数据点
x_data = np.linspace(-np.pi, np.pi, 64, endpoint=True)
# 将整个figure分成两行两列，第三个参数表示将图形放在第1个网格中
# 沿着正弦曲线绘制散点图
plt.scatter(x_data,
            np.sin(x_data),
            c='purple',
            s=50,
            alpha=0.5,
            marker='p',
            linewidths=1,
            edgecolors=['green', 'yellow'])
# 绘制第二个散点图（只包含一个起点），突出起点
plt.scatter(x_data[0], np.sin(x_data)[0], c='red', s=150, alpha=1)
# 绘制第三个散点图（只包含一个结束点），突出结束点
plt.scatter(x_data[63], np.sin(x_data)[63], c='black', s=150, alpha=1)
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.gca().spines['bottom'].set_position(('data', 0))
plt.gca().spines['left'].set_position(('data', 0))
plt.title('正弦曲线的散点图')
plt.show()

