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
        layout.addWidget(self.vp_widget)


    def set_file(self, file_path: str):
        from ovito import scene

        for pipeline in scene.pipelines:
            pipeline.remove_from_scene()
        
        self.__new_pipeline(file_path)


    def set_occuppancy(self, occupancy_mode: int):
        from ovito import scene
        from ovito.modifiers import ExpressionSelectionModifier

        for pipeline in scene.pipelines:
            for modifier in pipeline.modifiers:
                if type(modifier) == ExpressionSelectionModifier:
                    modifier.expression = 'Occupancy.'+str(occupancy_mode)


    def __new_pipeline(self, file_path: str):
        from ovito.io import import_file
        from ovito.modifiers import ExpressionSelectionModifier, WignerSeitzAnalysisModifier

        pipeline = import_file(file_path)
        pipeline.modifiers.append(
            WignerSeitzAnalysisModifier(
                per_type_occupancies = True,
                output_displaced = True
            )
        )
        pipeline.modifiers.append(
            ExpressionSelectionModifier(
                    expression = 'Occupancy.1'
            )
        )
        pipeline.add_to_scene()
        self.vp.zoom_all((self.vp_widget.width(), self.vp_widget.height()))

global render_3d
render_3d = Render3D()