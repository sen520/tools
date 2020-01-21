import matplotlib.pyplot as plt
import numpy as np

"""
用 plot 方法画出 x=(0,10)间 sin 的图像 
3.用点加线的方式画出 x=(0,10)间 sin 的图像 
4.用 scatter 方法画出 x=(0,10)间 sin 的点图像 
5.用饼图的面积及颜色展示一组 4 维数据 
6.绘制一组误差为 ±0.8 的数据的误差条图 
7.绘制一个柱状图 
8.绘制一个水平方向柱状图
"""
# x = np.linspace(0, 10, 30)
# plt.plot(x, np.sin(x))
# plt.show()
# plt.plot(x, np.sin(x), '-o')
# plt.show()
#
#
# rng = np.random.RandomState(0)
# x = rng.randn(100)
# y = rng.randn(100)
# colors = rng.rand(100)
# sizes = 1000 * rng.rand(100)
#
# plt.scatter(x, y, c=colors, s=sizes, alpha=0.3, cmap='viridis')
# plt.colorbar()
# plt.show()

"""================================================================"""

# x = np.linspace(0, 10, 50)
# dy = 0.8
# y = np.sin(x) + dy * np.random.randn(50)
# plt.errorbar(x, y, yerr=dy, fmt='.k')
# plt.show()

"""================================================================"""


# x = [1, 2, 3, 4, 5, 6, 7, 8]
# y = [3, 1, 4, 5, 8, 9, 7, 2]
# label = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
#
# plt.bar(x, y, tick_label=label)
# plt.show()

"""================================================================"""

# x = [1, 2, 3, 4, 5, 6, 7, 8]
# y = [3, 1, 4, 5, 8, 9, 7, 2]
# label = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
#
# plt.barh(x, y, tick_label=label)
# plt.show()


"""
绘制 1000 个随机值的直方图 10.设置直方图分 30 个 bins，并设置为频率分布 
11.在一张图中绘制 3 组不同的直方图，并设置透明度 
12.绘制一张二维直方图 
13.绘制一张设置网格大小为 30 的六角形直方图
"""
# data = np.random.randn(1000)
# plt.hist(data)
# plt.show()

# data = np.random.randn(1000)
# plt.hist(data, bins=30, histtype='stepfilled', density=True)
# plt.show()

"""================================================================"""


# x1 = np.random.normal(0, 0.8, 1000)
# x2 = np.random.normal(-2, 1, 1000)
# x3 = np.random.normal(3, 2, 1000)
#
# kwargs = dict(alpha=0.3, bins=40, density=True)
#
# plt.hist(x1, **kwargs)
# plt.hist(x2, **kwargs)
# plt.hist(x3, **kwargs)
# plt.show()

"""================================================================"""


# mean = [0, 0]
# cov = [[1, 1], [1, 2]]
# x, y = np.random.multivariate_normal(mean, cov, 10000).T
# plt.hist2d(x, y, bins=30)
# plt.show()
# plt.hexbin(x, y, gridsize=30)
# plt.show()


"""
绘制 x=(0,10)间 sin 的图像，设置线性为虚线 15 设置 y 轴显示范围为(-1.5,1.5) 
16.设置 x,y 轴标签 variable x，value y 
17.设置图表标题“三角函数” 
18.显示网格 
19.绘制平行于 x 轴 y=0.8 的水平参考线 
20.绘制垂直于 x 轴 x<4 and x>6 的参考区域，以及 y 轴 y<0.2 and y>-0.2 的参考区域 
21.添加注释文字 sin(x) 
22.用箭头标出第一个峰值
"""
# x = np.linspace(0,10, 100)
# plt.plot(x, np.sin(x), '--')
# plt.show()

"""================================================================"""


# x = np.linspace(0, 10, 100)
# plt.plot(x, np.sin(x))
# plt.ylim(-1.5, 1.5)
# plt.show()

"""================================================================"""


# x = np.linspace(0.05, 10, 100)
# y = np.sin(x)
# plt.plot(x, y, label='sin(x)')
# plt.xlabel('variable x')
# plt.ylabel('value y')
# plt.show()

"""================================================================"""


# plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
# plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
# x = np.linspace(0.05, 10, 100)
# y = np.sin(x)
# plt.plot(x, y, label='sin(x)')
# plt.title('三角函数')
# plt.show()

"""================================================================"""

# x = np.linspace(0.05, 10, 100)
# y = np.sin(x)
# plt.plot(x, y)
# plt.grid()
# plt.show()

"""================================================================"""

# x = np.linspace(0.05, 10, 100)
# y = np.sin(x)
# plt.plot(x, y)
# plt.axhline(y=0.8, ls='--', c='r')
# plt.show()

"""================================================================"""

# x = np.linspace(0.05, 10, 100)
# y = np.sin(x)
# plt.plot(x, y)
# plt.axvspan(xmin=4, xmax=6, facecolor='r', alpha=0.3)
# plt.axhspan(ymin=-0.2, ymax=0.2, facecolor='y', alpha=0.3)
# plt.show()

"""================================================================"""

# x = np.linspace(0.05, 10, 100)
# y = np.sin(x)
# plt.plot(x, y)
# plt.text(3.2, 0, 'sin(x)', weight='bold', color='r')
# plt.show()

"""================================================================"""

# x = np.linspace(0.05, 10, 100)
# y = np.sin(x)
# plt.plot(x, y)
# plt.annotate('maximum', xy=(np.pi / 2, 1), xytext=(np.pi / 2 + 1, 1),
#              weight='bold',
#              color='r',
#              arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='r'))
# plt.show()

"""
在一张图里绘制 sin,cos 的图形，并展示图例 
24.调整图例在左上角展示，且不显示边框 
25.调整图例在画面下方居中展示，且分成 2 列 
26.绘制 sin(x),sin(x+π/2),sin(x+π)的图像，并只显示前 2 者的图例 
27.将图例分不同的区域展示
"""
# x = np.linspace(0, 10, 1000)
# fig, ax = plt.subplots()
# ax.plot(x, np.sin(x), label='sin')
# ax.plot(x, np.cos(x), '--', label='cos')
# # ax.legend()
# # ax.legend(loc='upper left', frameon=False)
# ax.legend(frameon=False, loc='lower center', ncol=2)
# plt.show()

"""================================================================"""

# x = np.linspace(0, 10, 1000)
# y = np.sin(x[:, np.newaxis] + np.pi * np.arange(0, 2, 0.5))
# # lines = plt.plot(x, y)
# # # lines 是 plt.Line2D 类型的实例的列表
# # plt.legend(lines[:2], ['first', 'second'])
# # plt.show()
# plt.plot(x, y[:, 0], label='first')
# plt.plot(x, y[:, 1], label='second')
# plt.plot(x, y[:, 2:])
# plt.legend(framealpha=1, frameon=True)
# plt.show()

"""================================================================"""

# fig, ax = plt.subplots()
# lines = []
# styles = ['-', '--', '-.', ':']
# x = np.linspace(0, 10, 1000)
# for i in range(4):
#     lines += ax.plot(x, np.sin(x - i * np.pi / 2), styles[i], color='black')
# ax.axis('equal')
#
# # 设置第一组标签
# ax.legend(lines[:2], ['line A', 'line B'], loc='upper right', frameon=False)
#
# # 创建第二组标签
# from matplotlib.legend import Legend
#
# leg = Legend(ax, lines[2:], ['line C', 'line D'], loc='lower right', frameon=False)
# ax.add_artist(leg)
# plt.show()


"""================================================================"""
"""
展示色阶 
29.改变配色为'gray' 
30.将色阶分成 6 个离散值显示"""
# x = np.linspace(0, 10, 1000)
# I = np.sin(x) * np.cos(x[:, np.newaxis])
# # plt.imshow(I)
# # plt.imshow(I, cmap='gray')
# plt.imshow(I, cmap=plt.cm.get_cmap('Blues', 6))
# plt.colorbar()
# plt.clim(-1, 1)
# plt.show()


# from mpl_toolkits import mplot3d
# fig = plt.figure()
# # ax = plt.axes(projection='3d')
# #
# # # Data for a three-dimensional line
# # zline = np.linspace(0, 15, 1000)
# # xline = np.sin(zline)
# # yline = np.cos(zline)
# # ax.plot3D(xline, yline, zline)
# ax = plt.axes(projection='3d')
# zdata = 15 * np.random.random(100)
# xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
# ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
# ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens')
# plt.show()
