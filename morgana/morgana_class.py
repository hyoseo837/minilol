from champ_class import champion
from bullet_class import bullet
import pygame
import os

class morgana(champion):
    
    def attack(self):
        if self.cool[0] <= 0:
            self.cool[0] = 1/self.stat[3]
            return bullet(self.name, self.ad, 500,\
                 (self.posx, self.posy), self.direction, 80)
    
    def skill1(self):
        if self.cool[1] <= 0:
            self.cool[1] = 6
            return bullet(self.name, self.ap*1.5, 600,\
                 (self.posx,self.posy), self.direction, 60, 1,["rooted", 2.5, False],number=1) 

    def skill2(self):
        if self.cool[2] <= 0:
            self.cool[2] = 10
            self.shield.append("black")
            return bullet(self.name, self.ap*2, 1000,\
                 (self.posx,self.posy), self.direction, 60, 2,["black",3],number=2)