import matplotlib.pyplot as plt
import numpy as np

delta = 0.025
# 生成代表x轴数据的列表
x = np.arange(-3.0, 3.0, delta)
# 生成代表y轴数据的列表
y = np.arange(-2.0, 2.0, delta)
# 对X、y数据进行网格化
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
# 计算Z轴数据（高度数据）
Z = (Z1 - Z2) * 2
# 为等高线图填充颜色，16指定将等高线分为几部分
plt.contourf(x, y, Z, 16, alpha=0.75, cmap='rainbow') # 使用颜色映射来区分不同高度的区域
# 绘制等高线
c = plt.contour(x, y, Z, 16, colors='black', linewidths=0.5)
# 绘制等高线数据
plt.clabel(c, inline=True, fontsize=10)
# 去除坐标轴
plt.xticks(())
plt.yticks(())
# 设置标题
plt.title('等高线图')
# 为两个坐标轴设置名称
plt.xlabel("纬度")
plt.ylabel("经度")
plt.show()

