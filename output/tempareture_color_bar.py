def create_tem_color_bar(tempareture = [0,1,2,3,4,5,6,7,8,9,20]):
    from matplotlib import pyplot as plt
    import matplotlib as mpl
    from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
    import numpy

    fig, ax = plt.subplots(figsize=(6, 1), layout='constrained')

    cmap = mpl.cm.hot
    norm = mpl.colors.Normalize(vmin=numpy.max(tempareture), vmax=numpy.min(tempareture))

    colorbar = fig.colorbar(
        mpl.cm.ScalarMappable(norm=norm, cmap=cmap),
        cax=ax, orientation='vertical')
    
    colorbar.set_label('K')

    widget = FigureCanvas(fig)
    return widget