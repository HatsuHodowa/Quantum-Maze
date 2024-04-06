from enum import Enum
import pygame

CELL_COLORS = {
    0 : pygame.Color(255, 255, 255),
    1 : pygame.Color(0, 0, 0),
    2 : pygame.Color(0, 0, 0),
    3 : pygame.Color(255, 255, 255),
    4 : pygame.Color(150, 150, 150),
    5 : pygame.Color(255, 255, 255),
    6 : pygame.Color(255, 255, 0),
    7 : pygame.Color(255, 255, 0),
    8 : pygame.Color(255, 255, 0)
}

class cell_type(Enum):
    PATH = 0
    WALL = 1
    ENTANGLED_BLOCK_1 = 2 
    ENTANGLED_BLOCK_2 = 3
    ENTANGLED_BLOCK_TRIGGER = 4
    SPAWN_POINT = 5
    CHECKPOINT_01 = 6
    CHECKPOINT_10 = 7
    CHECKPOINT_11 = 8
    
