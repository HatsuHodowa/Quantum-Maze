import pygame 
import sys
import time

# importing modules
sys.path.append("..")
sys.path.append("resources")

import cell_type
import SampleLevels

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
        goal_position = (level.player_coord[0] + to_move[0], level.player_coord[1] + to_move[1])
        if goal_position[0] > 9 or goal_position[0] < 0:
            return
        if goal_position[1] > 9 or goal_position[1] < 0:
            return
        
        # checking tiles
        cell_value = level.get_coord_value(goal_position[0], goal_position[1])
        if cell_value == 1:
            return

        # moving player
        level.player_coord = goal_position

    def process_current_square(self):
        level = self.display.level
        player_coords = level.player_coords
        