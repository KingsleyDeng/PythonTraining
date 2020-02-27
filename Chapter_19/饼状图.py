import matplotlib.pyplot as plt

# 准备数据
data = [
    0.15004, 0.13300, 0.08530, 0.07384, 0.04624, 0.04483, 0.02716, 0.02567,
    0.02224, 0.01479, 0.37689
]
# 准备标签
labels = [
    'Java', 'C', 'Python', 'C++', 'Visual Basic.NET', 'C#', 'JavaScript',
    'PHP', 'SQL', 'Assembly language', '其他'
]
# 将排在第3位的语言（Python）分离出来
explode = [0, 0, 0.3, 0, 0, 0, 0, 0, 0, 0, 0]
# 使用自定义颜色
colors = ['red', 'pink', 'magenta', 'purple', 'orange']
# 将横、纵坐标轴标准化处理，保证饼图是一个正圆，否则为椭圆
plt.axes(aspect='equal')
# 控制X轴和Y轴的范围（用于控制饼图的圆心、半径）
plt.xlim(0, 8)
plt.ylim(0, 8)

# 绘制饼图
plt.pie(x=data, # 绘图数据
        labels=labels, # 添加编程语言标签
        explode=explode, # 突出显示Python
        colors=colors, # 设置饼图的自定义填充色
        autopct='%.3f%%', # 设置百分比的格式，此处保留3位小数
        pctdistance=0.8, # 设置百分比标签与圆心的距离
        labeldistance=1.05, # 设置标签与圆心的距离
        startangle=180, # 设置饼图的初始角度
        center=(4, 4), # 设置饼图的圆心（相当于X轴和Y轴的范围）
        radius=3.8, # 设置饼图的半径（相当于X轴和Y轴的范围
        counterclock=False, # 是否为逆时针方向，这里为顺时针
        wedgeprops={
            'linewidth': 1,
            'edgecolor': 'green'
        }, # 设置饼图内外边界的属性值
        textprops={
            'fontsize': 12,
            'color': 'black'
        }, # 设置文本标签的属性值
        frame=1) # 是否显示饼图的圆圈，此处设置为显示
# 不显示X轴和Y轴的刻度值
plt.xticks(())
plt.yticks(())
# 添加图形标题
plt.title('TIOBE2019年6月编程语言指数排行榜前10名')
# 显示图形
plt.show()