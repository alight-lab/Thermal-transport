import os
os.environ['OVITO_GUI_MODE'] = '1'

from GUI.main_window import MainWindow
from output.render_3d import render_3d

from PySide6.QtWidgets import QApplication, QWidget
from ovito.vis import Viewport
import sys


app = QApplication(sys.argv)
window = MainWindow()
window.show()
# set_file('data\lattice.lmp')
vp = Viewport(type=Viewport.Type.Ortho, camera_dir=(2, 1, -1))
vp_widget = vp.create_qt_widget()
window.verticalLayout_7.addWidget(vp_widget)
vp.zoom_all((vp_widget.width(), vp_widget.height()))



sys.exit(app.exec())