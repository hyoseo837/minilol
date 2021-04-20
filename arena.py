import pygame
import math
import random
import os
import stats
from bullet_class import bullet

loc = os.path.dirname(os.path.abspath(__file__))
white_block = pygame.image.load(f"{loc}/a_stack.png")
player1, player2 = "player 1","player 2"
picked = []
lucianR = False
lrcount = 0
ldir = None
luspeed = 7
akaliR = -1

def pick(turn):
    if turn == 1:
        player = player1
    elif turn == 0:
        player = player2
    while True:
        ppick = input(f"{player} pick : ")
        if ppick in stats.stat_list.keys() and ppick not in picked:
            if ppick == "morgana":
                from morgana.morgana_class import morgana
                picked.append(ppick)
                return morgana(ppick, (1200 - turn*800,400), 90)

            elif ppick == "udyr":
                from udyr.udyr_class import udyr
                picked.append(ppick)
                return udyr(ppick, (1200 - turn*800,400), 90)

            elif ppick == "lucian":
                from lucian.lucian_class import lucian
                picked.append(ppick)
                return lucian(ppick, (1200 - turn*800,400), 90)

            elif ppick == "akali":
                from akali.akali_class import akali
                picked.append(ppick)
                return akali(ppick, (1200 - turn*800,400), 90)
                
            elif ppick == "annie":
                from annie.annie_class import annie
                picked.append(ppick)
                return annie(ppick, (1200 - turn*800,400), 90)


print("\n\n\n")
for i in list(sorted(stats.stat_list.keys())):
    print(i)
print("\n")
player1 = pick(1)

print("\n\n\n")
for i in list(sorted(stats.stat_list.keys())):
    if i not in picked:
        print(i)
print("\n")
player2 = pick(0)

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
                if akaliR > 0:
                    if akali == player1:
                        pass
                    else:
                        md1 = -1
                else:
                    md1 = -1
        if keys_pressed[pygame.K_a]:
            if player1.status != "stunned":
                td1 = 1
        if keys_pressed[pygame.K_d]:
            if player1.status != "stunned":
                td1 = -1
        if keys_pressed[pygame.K_g]:
            if player1.status != "stunned":
                k = player1.attack()
                if k == None:
                    pass
                else:
                    if player1.name == "lucian":
                        lucianR = True
                        lucian = player1
                        lrcount = luspeed*2
                        ldir = lucian.direction
                        continue
                    bullets.append(k)
        if keys_pressed[pygame.K_h]:
            if player1.status != "stunned":
                k = player1.skill1()
                if k == None:
                    pass
                else:
                    bullets.append(k)
        if keys_pressed[pygame.K_j]:
            if player1.status != "stunned":
                k = player1.skill2()
                if k == None:
                    pass
                else:
                    if player1.name == "lucian":
                        lucianR = True
                        lucian = player1
                        lrcount = luspeed*15
                        ldir = lucian.direction
                        continue
                    if player1.name == "akali":
                        akaliR = 6
                        akali = player1
                    bullets.append(k)

    if True: # player 2 input
        md2,td2 = 0,0
        if keys_pressed[pygame.K_UP]:
            if player2.status == "none":
                md2 = 1
        if keys_pressed[pygame.K_DOWN]:
            if player2.status == "none":
                if akaliR > 0:
                    if akali == player2:
                        pass
                    else:
                        md2 = -1
                else:
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
                    if player2.name == "lucian":
                        lucianR = True
                        lucian = player2
                        lrcount = luspeed*2
                        ldir = lucian.direction
                        continue
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
                    if player2.name == "lucian":
                        lucianR = True
                        lucian = player2
                        lrcount = luspeed*15
                        ldir = lucian.direction
                        continue
                    if player2.name == "akali":
                        akaliR = 8
                        akali = player2
                    bullets.append(k)

    if lucianR :
        if lrcount%luspeed == 0:
            if lucian.status != "stunned":
                bullets.append(bullet(lucian.name, lucian.ad*0.4, 300,(lucian.posx, lucian.posy), ldir, 90))
        lrcount -= 1
        if lrcount <= 0:
            lucianR = False

    if akaliR > 0:
        akaliR -= 1
        akali.speed  =  200
        akali.move(1,dt)
        if akaliR < 0:
            akali.speed = akali.stat[2]
            akaliR = -1

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
        if i.name == "annie":
            for k in range(i.stack):
                screen.blit(pygame.transform.scale(white_block,(10,6)), (i.posx+k*12-23,i.posy-25))
    for i in bullets:
        screen.blit(i.rsprite, (i.posx - i.sprite.get_rect().size[0]/2, i.posy- i.sprite.get_rect().size[1]/2))
    
    
    
    pygame.display.update() 


pygame.quit()