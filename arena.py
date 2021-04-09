import pygame
import math
import random
import os

from morgana.morgana_class import morgana
from udyr.udyr_class import udyr

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

background = pygame.image.load(f"{loc}/background.png")

player1 = udyr("udyr", (400,400), 0, "none") # wasd ghj
player2 = morgana("morgana", (800,400), 180, "none") # arrow 123
md1,td1 = 0,0
md2,td2 = 0,0

# Time Variable
# [Moment Name] = pygame.time.get_ticks() # Save the moment

running = True
while running:

    dt = clock.tick(60)
    player1.update(md1,td1,dt)
    player2.update(md2,td2,dt)

    for i in [player1,player2]:
        i.hp_text = hp_font.render(f"{i.hp}",True, (10,10,10))

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
    
    keys_pressed = pygame.key.get_pressed()
    md1,td1 = 0,0
    if keys_pressed[pygame.K_w]:
        md1 = 1
    if keys_pressed[pygame.K_s]:
        md1 = -1
    if keys_pressed[pygame.K_a]:
        td1 = 1
    if keys_pressed[pygame.K_d]:
        td1 = -1
    if keys_pressed[pygame.K_g]:
        k = player1.attack()
        if k == None:
            pass
        else:
            bullets.append(k)

    md2,td2 = 0,0
    if keys_pressed[pygame.K_UP]:
        md2 = 1
    if keys_pressed[pygame.K_DOWN]:
        md2 = -1
    if keys_pressed[pygame.K_LEFT]:
        td2 = 1
    if keys_pressed[pygame.K_RIGHT]:
        td2 = -1
    if keys_pressed[pygame.K_KP1]:
        k = player2.attack()
        if k == None:
            pass
        else:
            bullets.append(k)
    if keys_pressed[pygame.K_KP2]:
        k = player2.skill1()
        if k == None:
            pass
        else:
            bullets.append(k)

    for i in bullets:
        i.move(dt)
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
    

    if player1.hp <= 0:
        print("player 2 win!")
        running = False 
    if player2.hp <= 0:
        print("player 1 win!")
        running = False 


    screen.blit(background, (0, 0))
    for i in bullets:
        screen.blit(i.rsprite, (i.posx - i.sprite.get_rect().size[0]/2, i.posy- i.sprite.get_rect().size[1]/2))

    screen.blit(player1.rsprite, (player1.rposx, player1.rposy))
    screen.blit(player1.hp_text, (player1.posx-15, player1.posy + 20))
    screen.blit(player2.rsprite, (player2.rposx, player2.rposy))
    screen.blit(player2.hp_text, (player2.posx-15, player2.posy + 20))
    
    pygame.display.update() 


pygame.quit()