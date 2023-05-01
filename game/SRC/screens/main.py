import pygame
from mpmath import *
from pygame import mixer
import random

pygame.init()
mixer.init()

class GameScreen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.font = pygame.font.Font(r"game\fonts\Savior3.ttf", 50)

        self.screen.fill((157, 157, 157))