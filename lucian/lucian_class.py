from champ_class import champion
from bullet_class import bullet
import pygame
import os

class lucian(champion):
    
    def attack(self):
        if self.cool[0] <= 0:
            self.cool[0] = 1/self.stat[3]
            return bullet(self.name, self.ad, 300,\
                 (self.posx, self.posy), self.direction, 80)

    
    def skill1(self):
        if self.cool[1] <= 0:
            self.cool[1] = 6
            return bullet(self.name, self.ad*0.1, 120,\
                 (self.posx,self.posy), self.direction, 50, 1,["", 2.5, True],number=1) 

    def skill2(self):
        if self.cool[2] <= 0:
            self.cool[2] = 24
            return bullet(self.name, self.ad*2, 1000,\
                 (self.posx,self.posy), self.direction, 60,number=2)