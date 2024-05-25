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


    def set_occupancy(
            self,
            reference_file:str,
            display_vacancy:bool=False,
            determin_occupancy=None | int,
            ):
        """ 
        `rederence_file`: 必须指定参照文件，指向未弛豫前文件；
        `display_vacancy`: 显示缺陷(`determin_occupancy=1`)，会强制切换至显示参照文件，否则无法正常显示；
        `determin_occupancy`: 指定occupancy，而不是大于等于2；
        """
        from ovito import scene
        from ovito.modifiers import ExpressionSelectionModifier, WignerSeitzAnalysisModifier
        from ovito.pipeline import ReferenceConfigurationModifier
        from ovito.pipeline import FileSource

        pipeline =  scene.selected_pipeline

        pipeline.modifiers.clear()

        output_displaced = True
        if display_vacancy == True or determin_occupancy == 0:
            output_displaced = False

        occupancy_modifier = WignerSeitzAnalysisModifier(
            output_displaced = output_displaced
            )

        occupancy_modifier.reference = FileSource()
        occupancy_modifier.reference.load(reference_file)

        pipeline.modifiers.append(occupancy_modifier)

        expression = 'Occupancy>=2'
        if type(determin_occupancy) == int:
            expression = 'Occupancy==' + str(determin_occupancy)
        if display_vacancy == True:
            expression = 'Occupancy==0'

        pipeline.modifiers.append(
            ExpressionSelectionModifier(
                expression = expression
            )
        )


    def set_color_by_tempareture(self, tempareture = [0,1,2,3,4,5,6,7,8,9,20]):
        from ovito import scene
        from ovito.modifiers import ColorCodingModifier
        from ovito.vis import TextLabelOverlay
        from matplotlib.colors import Normalize
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


    def render_png(self, filename:str, reference_file:str, tempareture=None):
        from ovito import scene
        if not scene.selected_pipeline == None:
            (prepend, suffix) = filename.split('.')
            self.vp.render_image(filename=filename)

            temp_render_3d = self
            if not tempareture == None:
                temp_render_3d.set_color_by_tempareture(tempareture)
                temp_render_3d.vp.render_image(
                    filename=prepend + '_依温度着色' + '.' + suffix
                    )
            
            temp_render_3d.set_occupancy(
                reference_file=reference_file
                )
            temp_render_3d.vp.render_image(
                filename=prepend + '_突出显示间隙' + '.' + suffix
                )
            temp_render_3d.set_occupancy(
                reference_file=reference_file,
                display_vacancy=True
                )
            temp_render_3d.vp.render_image(
                filename=prepend + '_突出显示空位' + '.' + suffix
            )


    def __new_pipeline(self, file_path: str):
        from ovito.io import import_file

        pipeline = import_file(file_path)
        pipeline.add_to_scene()
        self.vp.zoom_all((self.vp_widget.width(), self.vp_widget.height()))
    

global render_3d
render_3d = Render3D()