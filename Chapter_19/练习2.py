import pygal

# 准备数据
data = [191400, 50000, 1000, 30000, 110000]
data1 = [365, 100, 125, 30, 200]
# 准备标签
labels = ['生活', '教育学习', '健身', '旅游', '娱乐']
# 创建pygal.Pie对象
pie = pygal.Pie()
# 采用循环为饼图添加数据
for i, per in enumerate(data):
    pie.add(labels[i], per)
pie.title = '2019年消费投入图'
# 设置将图例放在底部
pie.legend_at_bottom = True
# 设置内圈的半径长度
pie.inner_radius = 0.4
# 指定将数据图输出到SVG文件中
pie.render_to_file('my.svg')

# 创建pygal.Pie对象
pie1 = pygal.Pie()
# 采用循环为饼图添加数据
for i, per in enumerate(data1):
    pie1.add(labels[i], per)
pie1.title = '2019年时间投入图'
# 设置将图例放在底部
pie1.legend_at_bottom = True
# 设置内圈的半径长度
pie1.inner_radius = 0.5
# 指定将数据图输出到SVG文件中
pie.render_to_file('my1.svg')

