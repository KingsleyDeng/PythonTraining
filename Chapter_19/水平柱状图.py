import matplotlib.pyplot as plt
import numpy as np

# 构建数据
x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
y_data2 = [52000, 54200, 51500, 58300, 56800, 59500, 62700]
bar_width = 0.3
# Y轴数据使用range(len(x_data))，也就是0、1、2、……
plt.barh(y=range(len(x_data)),
         width=y_data,
         label='产品1',
         color='steelblue',
         alpha=0.8,
         height=bar_width)
# Y轴数据使用np.arange(len(x_data)) + bar_width，也就是bar_width、1+bar_width、2+bar_width……
plt.barh(y=np.arange(len(x_data)) + bar_width,
         width=y_data2,
         label='产品2',
         color='indianred',
         alpha=0.8,
         height=bar_width)
# 在柱状图上显示具体的数值，ha参数控制水平对齐方式，va参数控制垂直对齐方式
for y, x in enumerate(y_data):
    plt.text(x + 5000,
             y - bar_width / 2,
             '%s' % x,
             ha='center',
             va='bottom')
for y, x in enumerate(y_data2):
    plt.text(x + 5000,
             y + bar_width / 2,
             '%s' % x,
             ha='center',
             va='bottom')
# 设置Y轴刻度
plt.yticks(np.arange(len(x_data)) + bar_width / 2, x_data)
# 设置标题
plt.title("产品比较")
# 为两个坐标轴设置名称
plt.xlabel("销量")
plt.ylabel("年份")
# 显示图例
plt.legend()
plt.show()

