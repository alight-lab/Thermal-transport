import os
os.environ['OVITO_GUI_MODE'] = '1'

from GUI.main_window import MainWindow
from output import render_3d

from PySide6.QtWidgets import QApplication
import sys
from ovito import scene
from ovito.modifiers import ColorCodingModifier

app = QApplication(sys.argv)
window = MainWindow()
window.show()

render_3d.insert_widget(window.painting_zoom)

sys.exit(app.exec())
