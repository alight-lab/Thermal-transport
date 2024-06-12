def plot_2d(x, y, xlabel, ylabel, ymin=None, ymax=None, savename=None, save_path=None, bar=None):
    import numpy as np
    from matplotlib import pyplot as plt
    from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
    fig = plt.figure()
    fig.patch.set_facecolor('w')
    cav = FigureCanvas(fig)
    ax = fig.subplots()
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    plt.subplots_adjust(bottom=0.3)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if ymin != None:
        plt.ylim(ymin - 25, ymax + 25)
    ax.grid(ls = "--", lw = 0.5, color = "#4E616C") # 背景线
    ax.plot(x, y, color='#00BFFF', linewidth=0.8)
    ax.patch.set_alpha(0)
    x_ticks = np.arange(min(x), max(x), (max(x) - min(x))/10)
    plt.xticks(x_ticks) # x坐标刻度
    if bar != None:
        for a, b in zip(x, y):
            plt.text(a, b, b, fontsize=5)

    # 保存图片和数据文件
    if savename != None:
        plt.savefig(save_path + '/' + savename + '.png')
        with open (save_path + '/' + savename + '.txt', 'w', encoding='UTF-8') as f:
            f.write('{:10}{:10}'.format(xlabel, ylabel))
            f.write('\n')
            for i in range(len(x)):
                data_x = round(x[i], 6)
                data_y = round(y[i], 6)
                f.write('{:10}{:10}'.format(str(data_x), str(data_y)))
                f.write('\n')

    plt.close('all')
    return cav

# x = [i*10.7 for i in range(1, 11)]
# for i in range(10):
#     x.append((i+1)*10.514+107)
# temp = '324.06 317.864 321.039 320.55 320.174 304.06 316.264 307.131 308.233 324.418 302.649 309.411 300.471 298.359 305.163 291.879 289.199 284.635 291.453 298.558'
# y = list(map(float, temp.split(' ')))                                                        
# from matplotlib import pyplot as plt
# plt.plot(x, y)
# plt.show()