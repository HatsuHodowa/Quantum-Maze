import pygame 
import sys
import time

# importing modules
sys.path.append("..")
sys.path.append("resources")

import cell_type
import SampleLevels
import grid_display

# variables
position = [0,0] # Some starting place for each level

class Model():
    def __init__(self, display):
        self.display = display
        self.last_keys = None
        
    def isOccupied(self) -> bool:
        pass
    
    def isSolved(self) -> bool:
        # puzzle = self.get_active_puzzle()
        # width, height = puzzle.get_width(), puzzle.get_height()
        # for x in range(width):
        #     for y in range(height):
        #         cell_type = puzzle.get_cell_type(x, y)
        #         if cell_type != Level.winning_cell:
        #             return False
        return True

    def isMoveIllegal(self, r, c) -> bool:
        
        pass
    
    def on_update(self, dt):

        # variables
        level = self.display.level

        # processing input
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and (self.last_keys == None or not self.last_keys[pygame.K_UP]):
            self.move_player((0, -1))
        if keys[pygame.K_DOWN] and (self.last_keys == None or not self.last_keys[pygame.K_DOWN]):
            self.move_player((0, 1))
        if keys[pygame.K_RIGHT] and (self.last_keys == None or not self.last_keys[pygame.K_RIGHT]):
            self.move_player((1, 0))
        if keys[pygame.K_LEFT] and (self.last_keys == None or not self.last_keys[pygame.K_LEFT]):
            self.move_player((-1, 0))

        # setting variables
        self.last_keys = keys

    def move_player(self, to_move):
        level = self.display.level

        # limiting player to grid
        goal_position = (level.player_coords[0] + to_move[0], level.player_coords[1] + to_move[1])
        if goal_position[0] > 9 or goal_position[0] < 0:
            return
        if goal_position[1] > 9 or goal_position[1] < 0:
            return
        
        # checking tiles
        cell_value = level.get_coord_value(goal_position[0], goal_position[1])
        if cell_value == 1:
            return

        # moving player
        level.player_coords = goal_position
        self.process_current_square()

    def process_current_square(self):

        # variables
        level = self.display.level
        player_coords = level.player_coords
        cell_value = level.get_coord_value(player_coords[0], player_coords[1])

        # checking cell value
        if cell_value == 4:
            print('trigger')
            for x in range(grid_display.GridDisplay.get_gridsize()):  # Assuming level has a width attribute
                for y in range(grid_display.GridDisplay.get_gridsize()):  # Assuming level has a height attribute
                    current_value = level.get_coord_value(x, y)
                    if current_value == 2:
                        level.set_coord_value(x, y, 3)
                    elif current_value == 3:
                        level.set_coord_value(x, y, 2)
            
        elif cell_value in [6, 7, 8, 9]:
            if cell_value == level.winning_cell:
                print('won!!!')
            else:
                print('lost!!!')
