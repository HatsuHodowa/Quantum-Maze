import pygame
import sys

# importing modules
sys.path.append("..")
sys.path.append("resources")
sys.path.append("model")

import cell_type
import model

# initializing pygame
pygame.init()
pygame.font.init()

# constants
GRID_SIZE = 10
WINDOW_PIXEL_SIZE = (500, 500)
MARGIN = 50
GRID_RECT = pygame.Rect(MARGIN, MARGIN, 500 - MARGIN * 2, 500 - MARGIN * 2)
CELL_SIZE = GRID_RECT.width / GRID_SIZE

class GridDisplay():
    def __init__(self, level):
        
        # properties
        self.window = pygame.display.set_mode(WINDOW_PIXEL_SIZE)
        self.clock = pygame.time.Clock()
        self.running = True

        self.level = level
        self.model = model.Model(self)

        # starting loop
        while self.running:
            dt = self.clock.tick(60) / 1000

            # event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # process model
            self.model.on_update(dt)

            # updating display
            self.update_display()

        pygame.quit()

    def update_display(self):

        # background
        self.window.fill("black")

        # creating grid
        if self.level != None:
            
            # looping grid cells
            for y_coord in range(GRID_SIZE):
                for x_coord in range(GRID_SIZE):

                    # creating rect for cell
                    cell_rect = pygame.Rect(
                        GRID_RECT.topleft[0] + x_coord * CELL_SIZE,
                        GRID_RECT.topleft[1] + y_coord * CELL_SIZE,
                        CELL_SIZE, CELL_SIZE
                    )
                    cell_value = self.level.get_coord_value(x_coord, y_coord)
                    cell_color = cell_type.CELL_COLORS[cell_value]
                    cell_color = cell_type.CELL_COLORS[cell_value]

                    # creating cell
                    pygame.draw.rect(self.window, cell_color, cell_rect, 0)

                    # drawing labels on winning cells
                    if cell_value in [5, 6, 7, 8, 9]:

                        # picking text
                        text = "|0>"
                        if cell_value == 7:
                            text = "|1>"
                        elif cell_value == 8:
                            text = "|->"
                        elif cell_value == 9:
                            text = "|+>"

                        # creating text
                        font = pygame.font.Font("robotomono.ttf", 20)
                        text = font.render(text=text, antialias=True, color=pygame.Color(0, 0, 0))
                        
                        self.window.blit(text, cell_rect)

        # drawing player
        player_coords = self.level.player_coords
        player_pixels = (
            GRID_RECT.topleft[0] + player_coords[0] * CELL_SIZE + CELL_SIZE / 2,
            GRID_RECT.topleft[1] + player_coords[1] * CELL_SIZE + CELL_SIZE / 2
        )
        pygame.draw.circle(self.window, pygame.Color(0, 255, 255), player_pixels, CELL_SIZE / 3, 0)

        # drawing box
        pygame.draw.rect(self.window, color="white", rect=GRID_RECT, width=1)

        # updating
        pygame.display.update()