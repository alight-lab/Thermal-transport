from typing import Any, Dict, Generator
from ovito.data import DataCollection
from ovito.pipeline import ModificationNode, ModifierInterface

class ColorByArrayModifier(ModifierInterface):
    def __init__(self, tempareture_array: list[float] = [0,1,2,3,4,5,6,7,8,9,20]) -> None:
        self.tempareture_array = tempareture_array
        self.__slice_to = len(tempareture_array)

        super().__init__()


    def modify(self, data: DataCollection, *, frame: int, input_slots: Dict[str, ModifierInterface.InputSlot], data_cache: DataCollection, pipeline_node: ModificationNode, **kwargs: Any) -> Generator[str | float, None, None] | None:
        positions_x = []
        for position in data.particles.positions:
            positions_x.append(position[0])

        max_position, min_position = __search_min_max(positions_x)
        diffrence_position = max_position - min_position
        
        color_array = __uniformization_array(self.tempareture_array)
        for (color, position) in (data.particles_.create_property('Color'), data.particles.positions):
            __index_color_array = type(int)((position - min_position) * self.__slice_to / diffrence_position)
            temp_color = color_array[__index_color_array]

            color[:] = (1-temp_color, 0, temp_color)

        return super().modify(data, frame=frame, input_slots=input_slots, data_cache=data_cache, pipeline_node=pipeline_node, **kwargs)
    

def __uniformization_array(array: list[float]):
    min_array, max_array = __search_min_max(array)
    diffrence = max_array - min_array
    for particle in array:
        particle = (particle-min_array)/diffrence

    return array


def __search_min_max(array: list[float]):
    max_array = 0
    min_array = 0
    for particle in array:
        if particle > max_array:
            max_array = particle
        elif particle < min_array:
            min_array = particle

    return (max_array,min_array)