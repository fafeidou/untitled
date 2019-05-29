# -*- coding=utf-8 -*


def ratio():
    labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    sizes = [15, 30, 45, 10]

    # 设置分离的距离，0表示不分离
    explode = (0, 0.1, 0, 0)

    pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)

    # Equal aspect ratio 保证画出的图是正圆形
    axis('equal')

    show()


from matplotlib.pyplot import bar, legend, show, axis, pie


def bat():
    size = 5
    a = np.random.random(size)
    b = np.random.random(size)
    c = np.random.random(size)
    x = np.arange(size)

    # 有多少个类型，只需更改n即可
    total_width, n = 0.8, 3
    width = total_width / n

    # 重新拟定x的坐标
    x = x - (total_width - width) / 2

    # 这里使用的是偏移
    bar(x, a, width=width, label='a')
    bar(x + width, b, width=width, label='b')
    bar(x + 2 * width, c, width=width, label='c')
    legend()
    show()


import numpy as np
import matplotlib.pyplot as plt


def grid():
    size = 5
    a = np.random.random(size)
    b = np.random.random(size)
    c = np.random.random(size)

    x = np.arange(size)

    # 这里使用的是偏移
    plt.bar(x, a, width=0.5, label='a', fc='r')
    plt.bar(x, b, bottom=a, width=0.5, label='b', fc='g')
    plt.bar(x, c, bottom=a + b, width=0.5, label='c', fc='b')

    plt.ylim(0, 2.5)
    plt.legend()
    plt.grid(True)
    plt.show()


def pie():
    # 设置每环的宽度
    size = 0.3
    vals = np.array([[60., 32.], [37., 40.], [29., 10.]])

    # 通过get_cmap随机获取颜色
    cmap = plt.get_cmap("tab20c")
    outer_colors = cmap(np.arange(3) * 4)
    inner_colors = cmap(np.array([1, 2, 5, 6, 9, 10]))

    print(vals.sum(axis=1))
    # [92. 77. 39.]

    plt.pie(vals.sum(axis=1), radius=1, colors=outer_colors,
            wedgeprops=dict(width=size, edgecolor='w'))
    print(vals.flatten())
    # [60. 32. 37. 40. 29. 10.]

    plt.pie(vals.flatten(), radius=1 - size, colors=inner_colors,
            wedgeprops=dict(width=size, edgecolor='w'))

    # equal 使得为正圆
    plt.axis('equal')
    plt.show()

import numpy as np
import matplotlib.pyplot as plt

def alphaRadio():
    np.random.seed(19680801)

    N = 10
    theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
    radii = 10 * np.random.rand(N)
    width = np.pi / 4 * np.random.rand(N)

    ax = plt.subplot(111, projection='polar')
    bars = ax.bar(theta, radii, width=width, bottom=0.0)
    # left表示从哪开始，
    # radii表示从中心点向边缘绘制的长度（半径）
    # width表示末端的弧长

    # 自定义颜色和不透明度
    for r, bar in zip(radii, bars):
        bar.set_facecolor(plt.cm.viridis(r / 10.))
        bar.set_alpha(0.5)

    plt.show()


from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def rainbowChat():
    fig = plt.figure()
    ax = Axes3D(fig)
    X = np.arange(-4, 4, 0.25)
    Y = np.arange(-4, 4, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(R)

    # 具体函数方法可用 help(function) 查看，如：help(ax.plot_surface)
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')

    plt.show()


# ratio()
# bat()
#
# grid()
# pie()
# alphaRadio()
rainbowChat()
