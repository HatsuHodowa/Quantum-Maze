import pygame
import sys

# importing modules
sys.path.append("..")
sys.path.append("resources")
sys.path.append("model")

import SampleLevels
import CellType

pygame.init()

# constants
GRID_SIZE = 10
WINDOW_PIXEL_SIZE = (500, 500)
MARGIN = 50
GRID_RECT = pygame.Rect(MARGIN, MARGIN, 500 - MARGIN * 2, 500 - MARGIN * 2)
CELL_SIZE = GRID_RECT.width / GRID_SIZE

class GridDisplay():
    def __init__(self):
        
        # properties
        self.window = pygame.display.set_mode(WINDOW_PIXEL_SIZE)
        self.clock = pygame.time.Clock()
        self.running = True

        self.current_grid = SampleLevels.XGate

        # starting loop
        while self.running:
            dt = self.clock.tick(30) / 1000

            # event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # updating display
            self.update_display()

        pygame.quit()

    def update_display(self):

        # background
        self.window.fill("black")

        # creating grid
        if self.current_grid != None:
            
            # looping grid cells
            for y_coord in range(GRID_SIZE):
                for x_coord in range(GRID_SIZE):

                    # creating rect for cell
                    cell_rect = pygame.Rect(
                        GRID_RECT.topleft[0] + x_coord * CELL_SIZE,
                        GRID_RECT.topleft[1] + y_coord * CELL_SIZE,
                        CELL_SIZE, CELL_SIZE
                    )
                    cell_value = self.current_grid.get_coord_value(x_coord, y_coord)
                    cell_color = CellType.CELL_COLORS[cell_value]

                    # creating cell
                    pygame.draw.rect(self.window, cell_color, cell_rect, 0)

        # drawing box
        pygame.draw.rect(self.window, color="white", rect=GRID_RECT, width=1)

        # updating
        pygame.display.update()

GridDisplay()