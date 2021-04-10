import pygame
import os
import math
# type 0: 평타 1:발사체, 2:쉴드
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
        elif type == 2:
            self.sprite = pygame.image.load(f"{loc}/{self.name}/skl2.png")

        self.damage = damage
        self.range = range
        self.initial_pos = pos
        self.direction = direction
        self.speed = speed
        if self.type == 2:
            self.direction = 0
            self.shield_time = self.option[1]
        self.rsprite = pygame.transform.rotate(self.sprite, self.direction)
        self.rect = self.rsprite.get_rect()
        self.rect.left = self.posx
        self.rect.top = self.posy
    
    def move(self,dt,user):
        if self.type != 2:
            self.posx += self.speed * math.cos(math.radians(self.direction))  *dt /100
            self.posy -= self.speed * math.sin(math.radians(self.direction))  *dt /100

            self.rsprite = pygame.transform.rotate(self.sprite, self.direction)
            self.rect = self.rsprite.get_rect()
            self.rect.left = self.posx
            self.rect.top = self.posy
        elif self.type == 2:
            self.shield_time -= 1/(1000/dt)
            self.posx,self.posy = user.posx, user.posy

    
    def effect(self, target, user):
        if self.type == 2:
            if self.shield_time < 0 :
                user.shield.remove("black")
            if "black" not in user.shield:
                return "remove"
        if self.rect.colliderect(target.rect):
            if self.type != 0:
                if "black" in target.shield:
                    target.shield.remove("black")
                    return "remove"
                else:
                    target.hp -= self.damage
                    if self.option[0] == "rooted":
                        target.rooted(self.option[1])
                    elif self.option[0] == "stunned":
                        target.stunned(self.option[1])
                    if not self.option[2]:
                        return "remove"
            else:
                target.hp -= self.damage
                return "remove"
