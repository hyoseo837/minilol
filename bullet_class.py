import pygame
import os
import math

loc = os.path.dirname(os.path.abspath(__file__))

class bullet:
    def __init__(self, name, damage, range, pos, direction, speed, type = 0):
        self.name = name
        self.posx, self.posy = pos
        if type == 0:
            self.sprite = pygame.image.load(f"{loc}/{name}/bullet.png")
        elif type == 1:
            self.sprite = pygame.image.load(f"{loc}/{name}/skl1.png")

        self.damage = damage
        self.range = range
        self.initial_pos = pos
        self.direction = direction
        self.speed = speed
    
    def move(self,dt):
        self.posx += self.speed * math.cos(math.radians(self.direction))  *dt /100
        self.posy -= self.speed * math.sin(math.radians(self.direction))  *dt /100

        self.rsprite = pygame.transform.rotate(self.sprite, self.direction)
        self.rect = self.rsprite.get_rect()
        self.rect.left = self.posx
        self.rect.top = self.posy