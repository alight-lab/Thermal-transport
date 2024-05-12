def set_file(file_path: str):
    from ovito import scene

    for pipeline in scene.pipelines:
        pipeline.remove_from_scene()
    
    _new_pipeline(file_path)


def set_occuppancy(occupancy_mode: int):
    from ovito import scene
    from ovito.modifiers import ExpressionSelectionModifier

    for pipeline in scene.pipelines:
        for modifier in pipeline.modifiers:
            if type(modifier) == ExpressionSelectionModifier:
                modifier.expression = 'Occupancy.'+str(occupancy_mode)


def _new_pipeline(file_path: str):
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
