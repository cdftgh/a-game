import pygame
pygame.init()

class TitleScreen:
    def __init__(self, width = 604, height = 480):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.font = pygame.font.Font(r"game\fonts\Savior2.ttf", 50)

        self.title_text = self.font.render("{game name}", True, (255, 255, 255))

        self.play_text = self.font.render("Press ENTER to Play, H for help", True, (255, 255, 255))

    def display(self):
        self.title_rect = self.title_text.get_rect(center=(self.width // 2, self.height // 3))
        self.play_rect = self.play_text.get_rect(center=(self.width // 2, self.height // 2))

        self.screen.blit(self.title_text, self.title_rect)
        self.screen.blit(self.play_text, self.play_rect)