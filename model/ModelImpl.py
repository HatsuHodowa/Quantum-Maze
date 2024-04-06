from Model import Model
import pygame 
import sys


position = [0,0] # Some starting place for each level

class ModelImpl(Model):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        square_position[1] -= square_speed
    if keys[pygame.K_DOWN]:
        square_position[1] += square_speed
    if keys[pygame.K_LEFT]:
        square_position[0] -= square_speed
    if keys[pygame.K_RIGHT]:
        square_position[0] += square_speed