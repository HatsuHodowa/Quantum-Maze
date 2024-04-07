import pygame
import pygame_gui
import pygame_gui.ui_manager
import sys

# importing modules
sys.path.append("..")
sys.path.append("resources")

import grid_display
import SampleLevels

# initializing pygame
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

        # other main properties
        self.button_events = {}

        # setting up window
        pygame.display.set_caption("Quantum Maze")
        self.set_window("main_menu")

        # starting
        while self.running:
            dt = self.clock.tick(30) / 1000

            # event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_object_id in self.button_events.keys():
                        self.button_events[event.ui_object_id]()

                self.ui_manager.process_events(event)

            # display
            self.ui_manager.update(dt)
            self.update_display()
            self.ui_manager.draw_ui(self.window)
            pygame.display.flip()

        pygame.quit()

    def set_window(self, window_name: str):
        self.ui_manager.clear_and_reset()
        if hasattr(self, window_name):
            getattr(self, window_name)()

    def main_menu(self):

        # creating ui elements
        title = pygame_gui.elements.UILabel(relative_rect=self.generate_scale_rect(0, 0.05, 0.8, 0.2),
            text="Quantum Maze", **self.default_kwargs, **self.center_anchor_kwargs)
        levels_button = pygame_gui.elements.UIButton(relative_rect=self.generate_scale_rect(0, 0.2, 0.8, 0.18),
            text="Select Level", object_id="levels_button", **self.default_kwargs, **self.center_anchor_kwargs)
        tutorial_button = pygame_gui.elements.UIButton(relative_rect=self.generate_scale_rect(0, 0.4, 0.8, 0.18),
            text="Tutorial", object_id="tutorial_button", **self.default_kwargs, **self.center_anchor_kwargs)
        credits_button = pygame_gui.elements.UIButton(relative_rect=self.generate_scale_rect(0, 0.6, 0.8, 0.18),
            text="Credits", object_id="credits_button", **self.default_kwargs, **self.center_anchor_kwargs)
        
        # button events
        def on_levels_button():
            self.set_window("levels_menu")

        self.button_events["levels_button"] = on_levels_button

    def levels_menu(self):

        # creating ui elements
        title = pygame_gui.elements.UILabel(relative_rect=self.generate_scale_rect(0, 0.05, 0.8, 0.2),
            text="All Levels", **self.default_kwargs, **self.center_anchor_kwargs)
        level1 = pygame_gui.elements.UIButton(relative_rect=self.generate_scale_rect(0, 0.2, 0.8, 0.14),
            text="Level 1 - X Gate", object_id="level1_button", **self.default_kwargs, **self.center_anchor_kwargs)
        level2 = pygame_gui.elements.UIButton(relative_rect=self.generate_scale_rect(0, 0.35, 0.8, 0.14),
            text="Level 2 - Z Gate", object_id="level2_button", **self.default_kwargs, **self.center_anchor_kwargs)
        level3 = pygame_gui.elements.UIButton(relative_rect=self.generate_scale_rect(0, 0.5, 0.8, 0.14),
            text="Level 3 - H Gate", object_id="level3_button", **self.default_kwargs, **self.center_anchor_kwargs)
        back_button = pygame_gui.elements.UIButton(relative_rect=self.generate_scale_rect(0, 0.65, 0.8, 0.14),
            text="Back", object_id="back_button", **self.default_kwargs, **self.center_anchor_kwargs)
        
        # button events
        def on_back_button():
            self.set_window("main_menu")

        def on_level1_button():
            self.ui_manager.clear_and_reset()
            grid_display.GridDisplay(SampleLevels.XGate, self)
            
        def on_level2_button():
            self.ui_manager.clear_and_reset()
            grid_display.GridDisplay(SampleLevels.ZGate, self)
            
        def on_level3_button():
            self.ui_manager.clear_and_reset()
            grid_display.GridDisplay(SampleLevels.HGate, self)

        self.button_events["back_button"] = on_back_button
        self.button_events["level1_button"] = on_level1_button
        self.button_events["level2_button"] = on_level2_button
        self.button_events["level3_button"] = on_level3_button

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