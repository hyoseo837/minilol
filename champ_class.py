import bullet_class
import pygame
import math
import os 
from stats import stat_list
loc = os.path.dirname(os.path.abspath(__file__))

screen_width = 1600
screen_height = 900

class champion:
    def __init__(self, name, position, direction, status):
        self.name = name
        self.posx , self.posy = position
        self.sprite = pygame.image.load(f"{loc}/{self.name}/body.png")
        self.rect = self.sprite.get_rect()
        self.rect.left = self.posx
        self.rect.top = self.posy

        self.direction = direction

        self.status = status
        self.root_time = -1
        self.atk_cool = 0
        self.skl1_cool = 0

        self.stat = stat_list[self.name]
        self.hp = self.stat[0]
        self.mp = self.stat[1]
        self.speed = self.stat[2]
        self.ad = self.stat[4]
        self.ap = self.stat[5]
    
    def move(self, alpha, dt):
            self.posx += self.speed * math.cos(math.radians(self.direction)) * alpha *dt /100
            self.posy -= self.speed * math.sin(math.radians(self.direction)) * alpha *dt /100

            if self.posx < 0 or self.posx > (screen_width - self.sprite.get_rect().size[0]):
                self.posx -= self.speed * math.cos(math.radians(self.direction)) * alpha *dt /100
            if self.posy < 0 or self.posy > (screen_height - self.sprite.get_rect().size[1]):
                self.posy += self.speed * math.sin(math.radians(self.direction)) * alpha *dt /100
    
    def turn(self, alpha,dt):
            self.direction += alpha * 3 * dt/20

    def update(self,al,be,dt):
        if self.status == "none":
            self.move(al,dt)
            self.turn(be,dt)
        self.rsprite = pygame.transform.rotate(self.sprite, self.direction)
        self.rect = self.rsprite.get_rect()
        self.rposx = self.posx-self.rect.size[0]/2
        self.rposy = self.posy-self.rect.size[1]/2
        self.rect.left = self.rposx
        self.rect.top = self.rposy
        
        if self.root_time > 0:
            self.status = "rooted"
            self.root_time -= 1/(1000/dt)
        else:
            self.status = "none"
            
        if self.atk_cool > 0:
            self.atk_cool -= 1/(1000/dt)
        if self.skl1_cool > 0:
            self.skl1_cool -= 1/(1000/dt)

    def attack(self):
        if self.atk_cool <= 0:
            bullets.append(bullet(self.name, self.stat[4], self.stat[6], (self.posx, self.posy), self.direction, 120))
            self.atk_cool = 1/self.stat[3]

    def rooted(self, length):
        self.status = "rooted"
        self.root_time = length
    
    def stunned(self, length):
        self.status = "stunned"
        self.stun_time = length