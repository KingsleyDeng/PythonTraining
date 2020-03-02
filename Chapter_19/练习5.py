import json
import pygal

pop_filename = 'exercise\\population-figures-by-country.json'
# 读取JSON格式的人口数据
with open(pop_filename) as f:
    pop_list = json.load(f)

# 构建时间数据
x_data = range(1970, 2017)
# 使用list列表依次保存中国、印度的人口
country_pops_list = [[], []]
for pop_dict in pop_list:
    # 获取中国的人口数据
    if pop_dict['Country_Code'] == 'CHN':
        for year in x_data:
            country_pops_list[0].append(pop_dict['Population_in_%d' % year] /
                                        10000)
    # 获取印度的人口数据
    if pop_dict['Country_Code'] == 'IND':
        for year in x_data:
            country_pops_list[1].append(pop_dict['Population_in_%d' % year] /
                                        10000)
# 定义国家名称列表
countries = ['中国', '印度']
# 创建pygal.Bar对象
bar = pygal.Bar()
# 采用循环添加代表条柱的数据
for i in range(len(countries)):
    bar.add(countries[i], country_pops_list[i])
bar.width = 1100
# 设置X轴的刻度值
bar.x_labels = x_data
bar.title = '1970-2016年中国印度人口对比'
bar.x_title = '年份'
bar.y_title = '人口（万）'
# 设置X轴的刻度值旋转45度
bar.x_label_rotation = 45
# 设置将图例放在底部
bar.legend_at_bottom = True
# 将数据图输出到文件
bar.render_to_file('population.svg')

