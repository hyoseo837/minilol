from champ_class import champion
from bullet_class import bullet
import pygame
import os

class annie(champion):
    def __init__(self, name, position, direction, status = "none"):
        super().__init__(name, position, direction, status)
        self.stack = 0
    
    def attack(self):
        if self.cool[0] <= 0:
            self.cool[0] = 1/self.stat[3]
            return bullet(self.name, self.ad, 350,\
                 (self.posx, self.posy), self.direction, 80)
    
    def skill1(self):
        if self.cool[1] <= 0:
            self.cool[1] = 3.5
            if self.stack == 4:
                self.stack = 0
                return bullet(self.name, self.ap*1.5, 400,\
                 (self.posx,self.posy), self.direction, 70, 1,["stunned", 1.5, False],number=1) 
            else:
                self.stack += 1
                return bullet(self.name, self.ap*1.5, 400,\
                 (self.posx,self.posy), self.direction, 70, 1,["", 0, False],number=1) 


    def skill2(self):
        if self.cool[2] <= 0:
            self.cool[2] = 5
            if self.stack == 4:
                self.stack = 0
                return bullet(self.name, self.ap*0.8, 60,\
                 (self.posx,self.posy), self.direction, 50, 1,["stunned", 1.5, True],number=2) 
            else:
                self.stack += 1
                return bullet(self.name, self.ap*0.8, 60,\
                 (self.posx,self.posy), self.direction, 50, 1,["", 2.5, True],number=2) 