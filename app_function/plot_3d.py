def plot_3d(ui):
    import sys
    from pathlib import PurePath
    from PySide6.QtCore import Qt
    from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QSlider, QVBoxLayout
    from gui_ui import Ui_Form
    import sys
    from PySide6.QtWidgets import QMainWindow, QApplication
    from ovito.vis import Viewport
    from ovito.modifiers import ExpressionSelectionModifier, WignerSeitzAnalysisModifier
    from ovito.io import import_file
    import ovito
    pipeline = import_file('data/Cu1.lmp')
    pipeline.modifiers.append(
            WignerSeitzAnalysisModifier(
                per_type_occupancies = True,
                output_displaced = True
                )
            )
    pipeline.modifiers.append(
                ExpressionSelectionModifier(
                    expression = 'Occupancy.0'
                    )
                )
    pipeline.add_to_scene()
    vp = Viewport(type=Viewport.Type.Ortho, camera_dir=(2, 1, -1))
    vp_widget = vp.create_qt_widget()
    ui.verticalLayout_7.addWidget(vp_widget)
    vp.zoom_all((vp_widget.width(), vp_widget.height()))
import sys
from pathlib import PurePath
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QSlider, QVBoxLayout
from gui_ui import Ui_Form
import sys
from PySide6.QtWidgets import QMainWindow, QApplication
app = QApplication(sys.argv)
mainwindow = QMainWindow()
ui = Ui_Form()
ui.setupUi(mainwindow)
mainwindow.show()
plot_3d(ui)
sys.exit(app.exec())