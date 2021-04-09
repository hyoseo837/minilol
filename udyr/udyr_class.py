from champ_class import champion
from bullet_class import bullet
import pygame
import os

class udyr(champion):
    
    def attack(self):
        if self.atk_cool <= 0:
            self.atk_cool = 1/self.stat[3]
            return bullet(self.name, self.ad, 50,\
                 (self.posx, self.posy), self.direction, 70)