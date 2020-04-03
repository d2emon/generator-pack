from ..cell import Cell


class PlantCell(Cell):
    default_name = 'plant cells'

    class Factory(Cell.Factory):
        pass
