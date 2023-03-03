import pygame
from constants import *
import os


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.images = []
        for i in range(1, 3):
            img = pygame.image.load(os.path.join('images', 'hero' + str(i) + '.png')).convert()
            img.convert_alpha()  # optimise alpha
            img.set_colorkey(ALPHA)  # set alpha
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()

    def control(self, x, y):
        """
        control player movement
        """
        self.movex += x
        self.movey += y

    def update(self):
        """
        Update sprite position
        """
        if self.border_check():
            self.rect.x = self.rect.x + self.movex
            self.rect.y = self.rect.y + self.movey
        # else:
            # self.rect.x -= 5
            # self.rect.y -= 5

        # # moving left
        # if self.movex < 0:
        #     self.frame += 1
        #     if self.frame > 3*ani:
        #         self.frame = 0
        #     self.image = pygame.transform.flip(self.images[self.frame//ani], True, False)
        #
        # # moving right
        # if self.movex > 0:
        #     self.frame += 1
        #     if self.frame > 3*ani:
        #         self.frame = 0
        #     self.image = self.images[self.frame//ani]

    def border_check(self):
        if (self.rect.x+30 < 650 and self.rect.y+30 < 400) or (self.rect.x-30 > WINDOW_WIDTH-870 and self.rect.y-30 < WINDOW_HEIGHT-400):
            return True
        return False
