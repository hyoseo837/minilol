from champ_class import champion
from bullet_class import bullet
import pygame
import os

class udyr(champion):
    
    def attack(self):
        if self.cool[0] <= 0:
            self.cool[0] = 1/self.stat[3]
            return bullet(self.name, self.ad, 70,\
                 (self.posx, self.posy), self.direction, 70,)

    
    def skill1(self):
        if self.cool[1] <= 0:
            self.cool[1] = 5
            return bullet(self.name, self.ap*1, 90,\
                 (self.posx,self.posy), self.direction, 60, 1,["stunned", 2, False])