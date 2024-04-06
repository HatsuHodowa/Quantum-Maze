import pygame
import pygame_gui
import time

import pygame_gui.ui_manager

pygame.init()

# main menu class
class MainMenu():
    def __init__(self):

        # gui properties
        self.window_size = (300, 300)

        # preparing window
        self.window = pygame.display.set_mode(self.window_size)
        self.ui_manager = pygame_gui.UIManager(self.window_size)
        self.clock = pygame.time.Clock()
        self.running = True

        # kwargs and properties
        self.default_kwargs = {"manager": self.ui_manager}
        self.center_anchor_kwargs = {"anchors": {"centerx": "centerx", "top": "top"}}

        # setting up window
        pygame.display.set_caption("Quantum Maze")

        # loading main menu
        self.current_window = {}
        self.open_main_menu()

        # starting
        while self.running:
            dt = self.clock.tick(30) / 1000

            # event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                self.ui_manager.process_events(event)

            # display
            self.ui_manager.update(dt)
            self.update_display()
            self.ui_manager.draw_ui(self.window)
            pygame.display.flip()

        pygame.quit()

    def clear_window(self):
        for item_name in self.current_window:
            window_item = self.current_window[item_name]

    def open_main_menu(self):
        self.clear_window()

        # creating ui elements
        self.current_window["title"] = pygame_gui.elements.UILabel(relative_rect=self.generate_scale_rect(0, 0.05, 0.8, 0.2),
            text="Quantum Maze", **self.default_kwargs, **self.center_anchor_kwargs)
        self.current_window["select_level"] = pygame_gui.elements.UIButton(relative_rect=self.generate_scale_rect(0, 0.25, 0.8, 0.2),
            text="Select Level", **self.default_kwargs, **self.center_anchor_kwargs)
        self.current_window["tutorial"] = pygame_gui.elements.UIButton(relative_rect=self.generate_scale_rect(0, 0.50, 0.8, 0.2),
            text="Tutorial", **self.default_kwargs, **self.center_anchor_kwargs)
        self.current_window["credits"] = pygame_gui.elements.UIButton(relative_rect=self.generate_scale_rect(0, 0.75, 0.8, 0.2),
            text="Credits", **self.default_kwargs, **self.center_anchor_kwargs)

    def generate_scale_rect(self, x_pos, y_pos, width, height):
        """Converts 4 positional and scale values from a proportion of the screen to an actual
        pixel amount using the scale_to_pixels function"""

        # creating rect
        x_pixels, y_pixels = self.scale_to_pixels(x_pos, y_pos)
        width_pixels, height_pixels = self.scale_to_pixels(width, height)
        rect = pygame.Rect(x_pixels, y_pixels, width_pixels, height_pixels)

        # returning
        return rect

    def scale_to_pixels(self, x_scale, y_scale):
        """Converts a proportional positional value from 0-1 for both x and y to a pixel value
        based on the current screen size (i.e. 0.5 is 50% of 500 pixels)"""

        # calculating pixels
        x_pixels = round(self.window_size[0] * x_scale)
        y_pixels = round(self.window_size[1] * y_scale)

        # returning
        return x_pixels, y_pixels

    def update_display(self):
        self.window.fill("black")

menu = MainMenu()