def plot_2d(x, y, xlabel, ylabel):
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
    ax.grid(alpha=0.1)
    ax.plot(x, y)
    ax.patch.set_alpha(0)
    return cav