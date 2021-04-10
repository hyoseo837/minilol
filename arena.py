import pygame
import math
import random
import os
import stats

loc = os.path.dirname(os.path.abspath(__file__))

print(list(stats.stat_list.keys()))
while True:
    p1_pick = input("player1 pick : ")
    if p1_pick in stats.stat_list.keys():
        if p1_pick == "morgana":
            from morgana.morgana_class import morgana
            player1 = morgana(p1_pick, (400,400), 0)
        elif p1_pick == "udyr":
            from udyr.udyr_class import udyr
            player1= udyr(p1_pick, (400,400), 0)
        break

print(list(stats.stat_list.keys()))
while True:
    p2_pick = input("player2 pick : ")
    if p2_pick in stats.stat_list.keys() and p2_pick != p1_pick:
        if p2_pick == "morgana":
            from morgana.morgana_class import morgana
            player2 = morgana(p2_pick, (1200,400), 0)
        elif p2_pick == "udyr":
            from udyr.udyr_class import udyr
            player2= udyr(p2_pick, (1200,400), 0)
        break




pygame.init()

screen_width = 1600
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("무야호 아레나")

clock = pygame.time.Clock()

bullets = []
# Text Variable
hp_font = pygame.font.Font(None, 20)
cool_font = pygame.font.Font(None, 50)

background = pygame.image.load(f"{loc}/background.png")

md1,td1 = 0,0
md2,td2 = 0,0
black = (0,0,0)
white = (221,221,221)

# Time Variable
# [Moment Name] = pygame.time.get_ticks() # Save the moment

running = True
while running:

    dt = clock.tick(60)
    player1.update(md1,td1,dt)
    player2.update(md2,td2,dt)

    for i in [player1,player2]:
        i.hp_text = hp_font.render(f"{round(i.hp)}",True, black)
        i.status_text = hp_font.render(f"{i.status}", True, black)

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
    
    if True: # player 1 input
        keys_pressed = pygame.key.get_pressed()
        md1,td1 = 0,0
        if keys_pressed[pygame.K_w]:
            if player1.status == "none":
                md1 = 1
        if keys_pressed[pygame.K_s]:
            if player1.status == "none":
                md1 = -1
        if keys_pressed[pygame.K_a]:
            if player1.status == "none":
                td1 = 1
        if keys_pressed[pygame.K_d]:
            if player1.status == "none":
                td1 = -1
        if keys_pressed[pygame.K_g]:
            if player1.status != "stunned":
                k = player1.attack()
                if k == None:
                    pass
                else:
                    bullets.append(k)
        if keys_pressed[pygame.K_h]:
            if player1.status != "stunned":
                k = player1.skill1()
                if k == None:
                    pass
                else:
                    bullets.append(k)
        if keys_pressed[pygame.K_j]:
            if player2.status != "stunned":
                k = player1.skill2()
                if k == None:
                    pass
                else:
                    bullets.append(k)

    if True: # player 2 input
        md2,td2 = 0,0
        if keys_pressed[pygame.K_UP]:
            if player2.status == "none":
                md2 = 1
        if keys_pressed[pygame.K_DOWN]:
            if player2.status == "none":
                md2 = -1
        if keys_pressed[pygame.K_LEFT]:
            if player2.status == "none":
                td2 = 1
        if keys_pressed[pygame.K_RIGHT]:
            if player2.status == "none":
                td2 = -1
        if keys_pressed[pygame.K_KP1]:
            if player2.status != "stunned":
                k = player2.attack()
                if k == None:
                    pass
                else:
                    bullets.append(k)
        if keys_pressed[pygame.K_KP2]:
            if player2.status != "stunned":
                k = player2.skill1()
                if k == None:
                    pass
                else:
                    bullets.append(k)
        if keys_pressed[pygame.K_KP3]:
            if player2.status != "stunned":
                k = player2.skill2()
                if k == None:
                    pass
                else:
                    bullets.append(k)

    for i in bullets:
        if i.name == player1.name:
            i.move(dt,player1)
        else:
            i.move(dt,player2)
        if (i.initial_pos[0] - i.posx)**2 + (i.initial_pos[1] - i.posy)**2 > i.range **2:
            bullets.remove(i)
        elif i.name == player1.name:
            if i.effect(player2,player1) == "remove":
                bullets.remove(i)
        elif i.name == player2.name:
            if i.effect(player1,player2) == "remove":
                bullets.remove(i)
    

    if player1.hp <= 0:
        print("player 2 win!")
        running = False 
    if player2.hp <= 0:
        print("player 1 win!")
        running = False 

    cool_texts1 = []
    for i in player1.cool:
        cool_texts1.append(cool_font.render(f"{round(i,2)}", True, black))
    cool_texts2 = []
    for i in player2.cool:
        cool_texts2.append(cool_font.render(f"{round(i,2)}", True, black))
        
    screen.blit(background, (0, 0))
    for i in bullets:
        screen.blit(i.rsprite, (i.posx - i.sprite.get_rect().size[0]/2, i.posy- i.sprite.get_rect().size[1]/2))
    
    for i in cool_texts1:
        screen.blit(i,(10, 50*cool_texts1.index(i)))
    for i in cool_texts2:
        screen.blit(i,(screen_width - i.get_rect().size[0]-10, 50*cool_texts2.index(i)))

    screen.blit(player1.rsprite, (player1.rposx, player1.rposy))
    screen.blit(player1.hp_text, (player1.posx-15, player1.posy + 20))
    
    screen.blit(player2.rsprite, (player2.rposx, player2.rposy))
    screen.blit(player2.hp_text, (player2.posx-15, player2.posy + 20))
    for i in [player1,player2]:
        if i.status != "none":
            screen.blit(i.status_text, (i.posx-20, i.posy-35))
    
    
    pygame.display.update() 


pygame.quit()