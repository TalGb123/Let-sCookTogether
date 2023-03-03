import pygame
from classes.Player import *
from constants import *
from functions import *
import os
from typing import Tuple


def main():
    pygame.init()
    background = pygame.image.load(os.path.join('images', 'temp kitchen.png'))
    background = pygame.transform.scale(background,
                                        (WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    pygame.init()
    backgroundbox = screen.get_rect()

    player = Player()  # spawn player
    player.rect.x = 0  # go to x
    player.rect.y = 0  # go to y
    player_list = pygame.sprite.Group()
    player_list.add(player)


    '''
    Main Loop
    '''
    running = True
    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == ord('q'):
                    pygame.quit()
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    player.control(-steps, 0)
                elif event.key == pygame.K_RIGHT or event.key == ord('d'):
                    player.control(steps, 0)
                if event.key == pygame.K_UP or event.key == ord('w'):
                    player.control(0, -steps)
                elif event.key == pygame.K_UP or event.key == ord('s'):
                    player.control(0, steps)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    player.control(steps, 0)
                elif event.key == pygame.K_RIGHT or event.key == ord('d'):
                    player.control(-steps, 0)
                if event.key == pygame.K_UP or event.key == ord('w'):
                    player.control(0, -steps)
                elif event.key == pygame.K_UP or event.key == ord('s'):
                    player.control(0, steps)

        screen.blit(background, backgroundbox)
        player.update()
        player_list.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


main()