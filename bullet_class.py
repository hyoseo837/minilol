import pygame
import os
import math

loc = os.path.dirname(os.path.abspath(__file__))

class bullet:
    def __init__(self, name, damage, range, pos, direction, speed, type = 0, option = []):
        self.name = name
        self.posx, self.posy = pos
        self.type = type
        self.option = option
        if type == 0:
            self.sprite = pygame.image.load(f"{loc}/{self.name}/bullet.png")
        elif type == 1:
            self.sprite = pygame.image.load(f"{loc}/{self.name}/skl1.png")

        self.damage = damage
        self.range = range
        self.initial_pos = pos
        self.direction = direction
        self.speed = speed
        self.rsprite = pygame.transform.rotate(self.sprite, self.direction)
        self.rect = self.rsprite.get_rect()
        self.rect.left = self.posx
        self.rect.top = self.posy
    
    def move(self,dt):
        self.posx += self.speed * math.cos(math.radians(self.direction))  *dt /100
        self.posy -= self.speed * math.sin(math.radians(self.direction))  *dt /100

        self.rsprite = pygame.transform.rotate(self.sprite, self.direction)
        self.rect = self.rsprite.get_rect()
        self.rect.left = self.posx
        self.rect.top = self.posy
    
    def effect(self, target):
    
        if self.rect.colliderect(target.rect):
            if self.type == 1:
                if self.option[0] == "rooted":
                    target.rooted(self.option[1])
                elif self.option[0] == "stunned":
                    target.stunned(self.option[1])
                if not self.option[2]:
                    return "remove"
            else:
                target.hp -= self.damage
                return "remove"
