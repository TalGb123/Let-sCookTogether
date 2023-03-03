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

    player_wasd = Player()  # spawn player
    player_arrows = Player() # spawn player
    player_wasd.rect.x = 150  # go to x
    player_wasd.rect.y = 220  # go to y
    player_arrows.rect.x = WINDOW_WIDTH-350 # go to x
    player_arrows.rect.y = 220  # go to y
    player_list = pygame.sprite.Group() # player list creation

    # adding players to the list
    player_list.add(player_wasd)
    player_list.add(player_arrows)

    '''
    Main Loop
    '''
    # pressed_keys = pygame.key.get_pressed()

    running = True
    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == ord('q') or event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    if event.key == ord('a'):
                        player_wasd.control(-steps, 0)
                    else:
                        player_arrows.control(-steps, 0)
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    if event.key == ord('d'):
                        player_wasd.control(steps, 0)
                    else:
                        player_arrows.control(steps, 0)
                if event.key == pygame.K_UP or event.key == ord('w'):
                    if event.key == ord('w'):
                        player_wasd.control(0, -steps)
                    else:
                        player_arrows.control(0, -steps)
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    if event.key == ord('s'):
                        player_wasd.control(0, steps)
                    else:
                        player_arrows.control(0, steps)

            if event.type == pygame.KEYUP:
                if event.key == ord('q') or event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    if event.key == ord('a'):
                        player_wasd.control(-steps, 0)
                    else:
                        player_arrows.control(-steps, 0)
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    if event.key == ord('d'):
                        player_wasd.control(steps, 0)
                    else:
                        player_arrows.control(steps, 0)
                if event.key == pygame.K_UP or event.key == ord('w'):
                    if event.key == ord('w'):
                        player_wasd.control(0, -steps)
                    else:
                        player_arrows.control(0, -steps)
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    if event.key == ord('s'):
                        player_wasd.control(0, steps)
                    else:
                        player_arrows.control(0, steps)

        screen.blit(background, backgroundbox)
        player_wasd.update()
        player_arrows.update()
        player_list.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


main()
