import champ_class
import bullet_class
import pygame
import os

class morgana(champ_class.champion):
    
    def attack(self):
        if self.atk_cool <= 0:
            self.atk_cool = 1/self.stat[3]
            return bullet_class.bullet(self.name, self.stat[4], 500, (self.posx, self.posy), self.direction, 60)