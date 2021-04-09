from champ_class import champion
from bullet_class import bullet
import pygame
import os

class morgana(champion):
    
    def attack(self):
        if self.atk_cool <= 0:
            self.atk_cool = 1/self.stat[3]
            return bullet(self.name, self.ad, 500,\
                 (self.posx, self.posy), self.direction, 80)
    
    def skill1(self):
        if self.skl1_cool <= 0:
            self.skl1_cool = 5
            return bullet(self.name, self.ap*2, 600,\
                 (self.posx,self.posy), self.direction, 60, 1,["rooted", 3, False]) #종류, 시간, 관통 여부