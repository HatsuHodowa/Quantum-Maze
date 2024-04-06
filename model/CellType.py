from enum import Enum

class CellType(Enum):
    PATH = 0
    WALL = 1
    ENTANGLED_BLOCK_1 = 2 
    ENTANGLED_BLOCK_2 = 3
    ENTANGLED_BLOCK_TRIGGER = 4
    SPAWN_POINT = 5
    CHECKPOINT_01 = 6
    CHECKPOINT_10 = 7
    CHECKPOINT_11 = 8
    
