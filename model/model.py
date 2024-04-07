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
        if cell_value == 1 or cell_value == 2:
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
            for x in range(grid_display.GridDisplay.get_gridsize()):  # Assuming level has a method to get grid size
                for y in range(grid_display.GridDisplay.get_gridsize()):
                    current_cell_value = level.get_coord_value(x, y)
                    if current_cell_value == 2:
                        level.set_coord_value(x, y, 0)
                    elif current_cell_value == 3:
                        level.set_coord_value(x, y, 1)
                    elif current_cell_value == 4:
                        level.set_coord_value(x, y, 0)

            self.display.notification("You have been entangled!!!!!")
            
        elif cell_value in [6, 7, 8, 9]:
            if cell_value == level.winning_cell:
                self.display.notification("You did it! You solved the thing!")
                print("Level completed. Returning to the menu...")
                self.running = False
                time.sleep(3.0)
                pygame.display.set_mode(self.menu.window_size)
        self.menu.set_window("levels_menu")
        return
        
        

    def reset(self):
        # Reset the current level to its initial state
        # This will require re-initializing the level object with its original grid
        self.level = Level(self.level.grid, self.level.winning_cell, self.level.name)
        self.model = Model(self)  # Re-initialize the model as well to reset player position and state
        print("Level reset. Try again!")
            else:
                self.display.notification("You didn't do it! You didn't solve the thing!")
                self.display.reset()