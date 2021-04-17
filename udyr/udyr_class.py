from champ_class import champion
from bullet_class import bullet
import pygame
import os

class udyr(champion):
    
    def attack(self):
        if self.cool[0] <= 0:
            self.cool[0] = 1/self.stat[3]
            return bullet(self.name, self.ad, 80,\
                 (self.posx, self.posy), self.direction, 100,)

    
    def skill1(self):
        if self.cool[1] <= 0:
            self.cool[1] = 5
            return bullet(self.name, self.ap*1, 100,\
                 (self.posx,self.posy), self.direction, 90, 1,["stunned", 2, False],number=1)

                 
    def skill2(self):
        if self.cool[2] <= 0:
            self.cool[2] = 5
            return bullet(self.name, self.ad*0.5, 100,\
                 (self.posx,self.posy), self.direction, 90, 1,["slowed",1, False, 50],number=2)