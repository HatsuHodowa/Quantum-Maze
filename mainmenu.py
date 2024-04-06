import pygame
import time

pygame.init()

# main menu class
class MainMenu():
    def __init__(self):

        # preparing window
        self.window = pygame.display.set_mode((500, 500))
        self.clock = pygame.time.Clock()
        self.running = True

        # starting
        while self.running:

            # event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # display
            self.update_display()
            pygame.display.flip()

            # framerate
            dt = self.clock.tick(15) / 1000

        pygame.quit()

    def update_display(self):
        pass

menu = MainMenu()