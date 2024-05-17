from PySide6.QtWidgets import QLayout

# Usage:
#     `from output.render_3d import render_3d`
#     then call these method in following

class Render3D(): 
    def __init__(self) -> None:
        from ovito.vis import Viewport

        self.vp = Viewport(type=Viewport.Type.Ortho, camera_dir=(2, 1, -1))
        


    def insert_widget(self, layout: QLayout):
        self.vp_widget = self.vp.create_qt_widget()
        layout.addWidget(self.vp_widget, 10)


    def set_file(self, file_path: str):
        from ovito import scene

        for pipeline in scene.pipelines:
            pipeline.remove_from_scene()
        
        self.__new_pipeline(file_path)


    def clear_modifiers(self):
        from ovito import scene
        
        for pipeline in scene.pipelines:
            pipeline.modifiers.clear()

        


    def set_occupancy(self, occupancy_mode: int):
        from ovito import scene
        from ovito.modifiers import ExpressionSelectionModifier, WignerSeitzAnalysisModifier

        for pipeline in scene.pipelines:
            pipeline.modifiers.clear()
            pipeline.modifiers.append(
                WignerSeitzAnalysisModifier(
                per_type_occupancies = True,
                output_displaced = True
                )
            )
            pipeline.modifiers.append(
                ExpressionSelectionModifier(
                    expression = 'Occupancy.' + str(occupancy_mode)
                )
            )

    def set_color_by_tempareture(self, tempareture = [0,1,2,3,4,5,6,7,8,9,20]):
        from ovito import scene
        from ovito.modifiers import ColorCodingModifier
        from ovito.vis import ColorLegendOverlay
        from ovito.qt_compat import QtCore
        from matplotlib.colors import Normalize, Colormap
        import matplotlib
        import numpy

        max_tempareture = numpy.max(tempareture)
        min_tempareture = numpy.min(tempareture)

        normalized_tempareture = Normalize(vmax=max_tempareture, vmin=min_tempareture)
        color_map = matplotlib.colormaps['hot']

        color_list = []
        for current in normalized_tempareture(tempareture):
            color_list.append(
                color_map(current)[:3]
            )

        for pipeline in scene.pipelines:
            pipeline.modifiers.clear()
            pipeline.modifiers.append(
                ColorCodingModifier(
                    property = 'Position.X',
                    gradient = ColorCodingModifier.Gradient(color_list)
                )
            )


    def __new_pipeline(self, file_path: str):
        from ovito.io import import_file
        from ovito.modifiers import ExpressionSelectionModifier, WignerSeitzAnalysisModifier

        pipeline = import_file(file_path)
        pipeline.add_to_scene()
        self.vp.zoom_all((self.vp_widget.width(), self.vp_widget.height()))

global render_3d
render_3d = Render3D()