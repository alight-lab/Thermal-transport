def plot_2d(x, y):
    from matplotlib import pyplot as plt
    from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
    fig = plt.figure()
    fig.patch.set_facecolor('#FFFFFF')
    cav = FigureCanvas(fig)
    ax = fig.subplots()
    # ax.set_facecolor('#FFFFFF')
    ax.plot(x, y)
    ax.patch.set_alpha(0)
    return cav