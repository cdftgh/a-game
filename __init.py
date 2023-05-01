from game.SRC.screens.title import TitleScreen
from game.SRC.screens.main import GameScreen
import pygame

title = TitleScreen()
clock = pygame.time.Clock()

main_screen = False

while True:
    if not main_screen:
        title.display()

    else:
        title = GameScreen(604, 480)

    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if keys[pygame.K_RETURN]:
            main_screen = True

    pygame.display.update()
    clock.tick(60)