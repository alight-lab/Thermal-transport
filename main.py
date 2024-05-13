import os
os.environ['OVITO_GUI_MODE'] = '1'

from GUI.main_window import MainWindow
from output.render_3d import render_3d

from PySide6.QtWidgets import QApplication, QWidget
import sys


app = QApplication(sys.argv)
window = MainWindow()
window.show()

render_3d.insert_widget(window.verticalLayout_7)


sys.exit(app.exec())