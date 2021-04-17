from champ_class import champion
from bullet_class import bullet
import pygame
import os

class akali(champion):
    def __init__(self, name, position, direction, status = "none"):
        super().__init__(name, position, direction, status)
        self.upgrade_attack = False
    
    def attack(self):
        if self.cool[0] <= 0:
            self.cool[0] = 1/self.stat[3]
            if self.upgrade_attack == True:
                self.upgrade_attack = False
                return bullet(self.name, self.ad + 0.5*self.ap, 100,\
                 (self.posx, self.posy), self.direction, 100)
            else:
                return bullet(self.name, self.ad, 80,\
                 (self.posx, self.posy), self.direction, 100)

    
    def skill1(self):
        if self.cool[1] <= 0:
            self.cool[1] = 2.5
            self.upgrade_attack = True
            return bullet(self.name, 0.7*self.ap, 120,\
                 (self.posx,self.posy), self.direction, 150, 1,["slowed", 0.5, True, 30],number=1) 

    def skill2(self):
        if self.cool[2] <= 0:
            self.cool[2] = 15
            return bullet(self.name, self.ap*2, 250,\
                 (self.posx,self.posy), self.direction, 200, 1,["",3,True],number=2)