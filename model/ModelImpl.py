from Model import Model
import pygame 
import sys


position = [0,0] # Some starting place for each level

class ModelImpl(Model):
    def __init__(self, library):
        if library is None:
            raise ValueError("Library cannot be None")
        self.library = library
        self.current = 0  # currentPuzzle
        puzzle = self.library.get_puzzle(self.current)
        self.lamp = [[0 for _ in range(puzzle.get_width())] for _ in range(puzzle.get_height())]
        self.observers = []
        
    def isOccupied(self) -> bool:
        pass
    
    def isSolved(self) -> bool:
        puzzle = self.get_active_puzzle()
        width, height = puzzle.get_width(), puzzle.get_height()
        pass
    
    def get_active_puzzle(self):
        return self.library.get_puzzle(self.current)
    
    
    def get_active_puzzle_index(self):
        return self.current
    
    def set_active_puzzle_index(self, index):
        if not (0 <= index < self.library.size()):
            raise IndexError("Puzzle index out of bounds")
        self.current = index
        self.reset_puzzle()
    
    def reset_puzzle(self):
        puzzle = self.library.get_puzzle(self.current)
        self.lamp = [[0 for _ in range(puzzle.get_width())] for _ in range(puzzle.get_height())]
        self.notify_observers()

    def isMoveIllegal(self, r, c) -> bool:
        
        pass
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] :
        square_position[1] -= square_speed
    if keys[pygame.K_DOWN]:
        square_position[1] += square_speed
    if keys[pygame.K_LEFT]:
        square_position[0] -= square_speed
    if keys[pygame.K_RIGHT]:
        square_position[0] += square_speed