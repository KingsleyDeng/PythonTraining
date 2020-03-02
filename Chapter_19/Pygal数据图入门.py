import pygal

x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
# 定义两个列表分别作为两组柱状图的Y轴数据
y_data = [5800, 60200, 63000, 71000, 84000, 90500, 107000]
y_data2 = [52000, 54200, 51500, 58300, 56800, 59500, 62700]
# 创建pygal.Bar对象
bar = pygal.Bar()
# 添加两组代表条柱的数据
bar.add('产品1', y_data)
bar.add('产品2', y_data2)
# 设置X轴的刻度值
bar.x_labels = x_data
bar._title = '产品历年销售量'
# 设置X,Y轴的标题
bar._x_title = '年份'
bar._y_title = '销量'
# 指定将数据图输出到SVG文件中
bar.render_to_file('pygal_bar_test.svg')

