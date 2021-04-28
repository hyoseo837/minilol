from champ_class import champion
from bullet_class import bullet
import pygame
import os

class mundo(champion):
    
    def attack(self):
        if self.cool[0] <= 0:
            self.cool[0] = 1/self.stat[3]
            return bullet(self.name, self.ad, 70,\
                 (self.posx, self.posy), self.direction, 100,)

    
    def skill1(self):
        if self.cool[1] <= 0:
            self.cool[1] = 5
            return bullet(self.name, self.ap*1, 250,\
                 (self.posx,self.posy), self.direction, 90, 1,["slowed", 1.5, False, 30],number=1)

                 
    def skill2(self):
        if self.cool[2] <= 0:
            self.cool[2] = 25
            return bullet(self.name, 0, 100,\
                 (self.posx,self.posy), self.direction, 90, 1,["",1, False, 50],number=2)