def plot_2d(x, y, xlabel, ylabel, legend):
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
    plt.close('all')
    return cav