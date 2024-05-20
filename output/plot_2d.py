def plot_2d(x, y, xlabel, ylabel, legend, savename):
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
    ax.grid(ls = "--", lw = 0.5, color = "#4E616C") # 背景线
    ax.plot(x, y, color='#00BFFF', linewidth=0.8)
    ax.patch.set_alpha(0)
    x_ticks = np.arange(min(x), max(x), (max(x) - min(x))/10)
    plt.legend([legend], loc='upper right') # 图例
    plt.xticks(x_ticks) # x坐标刻度
    
    # 保存图片和数据文件
    plt.savefig('data/' + savename + '.png')
    with open ('data/' + savename + '.txt', 'w') as f:
        f.write('{:10}{:10}'.format(xlabel, ylabel))
        f.write('\n')
        for i in range(len(x)):
            data_x = round(x[i], 6)
            data_y = round(y[i], 6)
            f.write('{:10}{:10}'.format(str(data_x), str(data_y)))
            f.write('\n')

    plt.close('all')
    return cav