import pygame
import math
import random
import os
from stats import stat_list
loc = os.path.dirname(os.path.abspath(__file__))
pygame.init()

screen_width = 1600
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("무야호 아레나")

clock = pygame.time.Clock()

bullets = []
# Text Variable
hp_font = pygame.font.Font(None, 20)

class bullet:
    def __init__(self, name, damage, range, pos, direction, speed):
        self.name = name
        self.posx, self.posy = pos
        self.sprite = pygame.image.load(f"{loc}/{name}/bullet.png")

        self.rect = self.sprite.get_rect()
        self.rect.left = self.posx
        self.rect.top = self.posy

        self.damage = damage
        self.range = range
        self.initial_pos = pos
        self.direction = direction
        self.speed = speed
    
    def move(self):
        self.posx += self.speed * math.cos(math.radians(self.direction))  *dt /100
        self.posy -= self.speed * math.sin(math.radians(self.direction))  *dt /100
        self.rect = self.sprite.get_rect()
        self.rect.left = self.posx
        self.rect.top = self.posy
        

class champion:
    def __init__(self, name, position, direction, status):
        self.name = name
        self.posx , self.posy = position
        self.sprite = pygame.image.load(f"{loc}/{name}/body.png")
        self.rect = self.sprite.get_rect()
        self.rect.left = self.posx
        self.rect.top = self.posy

        self.direction = direction

        self.status = status
        self.atk_cool = 0

        self.stat = stat_list[self.name]
        self.hp = self.stat[0]
        self.mp = self.stat[1]
        self.speed = self.stat[2]
    
    def move(self, alpha):
        self.posx += self.speed * math.cos(math.radians(self.direction)) * alpha *dt /100
        self.posy -= self.speed * math.sin(math.radians(self.direction)) * alpha *dt /100

        if self.posx < 0 or self.posx > (screen_width - self.sprite.get_rect().size[0]):
            self.posx -= self.speed * math.cos(math.radians(self.direction)) * alpha *dt /100
        if self.posy < 0 or self.posy > (screen_height - self.sprite.get_rect().size[1]):
            self.posy += self.speed * math.sin(math.radians(self.direction)) * alpha *dt /100
    
    def turn(self, alpha):
        self.direction += alpha * 3 * dt/20

    def update(self,al,be):
        self.move(al)
        self.turn(be)
        self.rsprite = pygame.transform.rotate(self.sprite, self.direction)
        self.rect = self.rsprite.get_rect()
        self.rposx = self.posx-player1.rect.size[0]/2
        self.rposy = self.posy-player1.rect.size[1]/2
        self.rect.left = self.rposx
        self.rect.top = self.rposy

        self.hp_text = hp_font.render(f"{self.hp}",True, (10,10,10))

        if self.atk_cool > 0:
            self.atk_cool -= 1/(1000/dt)

    def attack(self):
        if self.atk_cool <= 0:
            bullets.append(bullet(self.name, self.stat[4], self.stat[6], (self.posx, self.posy), self.direction, self.stat[7]))
            self.atk_cool = 1/self.stat[3]


background = pygame.image.load(f"{loc}/background.png")
player1 = champion("test", (400,400), 0, "none") # wasd ghj
player2 = champion("test2", (800,400), 180, "none") # arrow 123
md1,td1 = 0,0
md2,td2 = 0,0

# Time Variable
# [Moment Name] = pygame.time.get_ticks() # Save the moment

running = True
while running:

    dt = clock.tick(60)
    player1.update(md1,td1)
    player2.update(md2,td2)

    for i in bullets:
        i.move()
        if (i.initial_pos[0] - i.posx)**2 + (i.initial_pos[1] - i.posy)**2 > i.range **2:
            bullets.remove(i)
        elif i.name == player1.name:
            if i.rect.colliderect(player2.rect):
                player2.hp -= i.damage
                bullets.remove(i)
        elif i.name == player2.name:
            if i.rect.colliderect(player1.rect):
                player1.hp -= i.damage
                bullets.remove(i)
    
    for i in [player1,player2]:
        if i.hp <= 0:
           print(f"{i.name} win")
           running = False 

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                md1 = 1
            elif event.key == pygame.K_s:
                md1 = -1
            elif event.key == pygame.K_a:
                td1 = 1
            elif event.key == pygame.K_d:
                td1 = -1
            elif event.key == pygame.K_g:
                player1.attack()

            elif event.key == pygame.K_UP:
                md2 = 1
            elif event.key == pygame.K_DOWN:
                md2 = -1
            elif event.key == pygame.K_LEFT:
                td2 = 1
            elif event.key == pygame.K_RIGHT:
                td2 = -1
            elif event.key == pygame.K_KP1:
                player2.attack()
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                md1 = 0
            elif event.key == pygame.K_s:
                md1 = 0
            elif event.key == pygame.K_a:
                td1 = 0
            elif event.key == pygame.K_d:
                td1 = 0
            elif event.key == pygame.K_UP:
                md2 = 0
            elif event.key == pygame.K_DOWN:
                md2 = 0
            elif event.key == pygame.K_LEFT:
                td2 = 0
            elif event.key == pygame.K_RIGHT:
                td2 = 0
    

    screen.blit(background, (0, 0))

    screen.blit(player1.rsprite, (player1.rposx, player1.rposy))
    screen.blit(player1.hp_text, (player1.posx-15, player1.posy + 20))
    screen.blit(player2.rsprite, (player2.rposx, player2.rposy))
    screen.blit(player2.hp_text, (player2.posx-15, player2.posy + 20))
    for i in bullets:
        screen.blit(i.sprite, (i.posx,i.posy))

    pygame.display.update() 


pygame.quit()