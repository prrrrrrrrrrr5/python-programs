import pygame
import sys
import random

pygame.init()

screen=pygame.display.set_mode((1150,650))
clock=pygame.time.Clock()

griglia=pygame.image.load(r"C:\Users\ivano\Desktop\Giochi Fatti Da Me\Python\Tic Tac Toe\immagini\griglia.png").convert_alpha()

croce=pygame.image.load(r"C:\Users\ivano\Desktop\Giochi Fatti Da Me\Python\Tic Tac Toe\immagini\croce.png").convert_alpha()
cerchio=pygame.image.load(r"C:\Users\ivano\Desktop\Giochi Fatti Da Me\Python\Tic Tac Toe\immagini\cerchio.png").convert_alpha()

quadrato1=pygame.image.load(r"C:\Users\ivano\Desktop\Giochi Fatti Da Me\Python\Tic Tac Toe\immagini\blank.png").convert_alpha()
quadrato1_rect=quadrato1.get_rect(topleft=(165,70))

quadrato2=pygame.image.load(r"C:\Users\ivano\Desktop\Giochi Fatti Da Me\Python\Tic Tac Toe\immagini\blank.png").convert_alpha()
quadrato2_rect=quadrato2.get_rect(topleft=(490,70))

quadrato3=pygame.image.load(r"C:\Users\ivano\Desktop\Giochi Fatti Da Me\Python\Tic Tac Toe\immagini\blank.png").convert_alpha()
quadrato3_rect=quadrato3.get_rect(topleft=(800,70))

quadrato4=pygame.image.load(r"C:\Users\ivano\Desktop\Giochi Fatti Da Me\Python\Tic Tac Toe\immagini\blank.png").convert_alpha()
quadrato4_rect=quadrato4.get_rect(topleft=(165,285))

quadrato5=pygame.image.load(r"C:\Users\ivano\Desktop\Giochi Fatti Da Me\Python\Tic Tac Toe\immagini\blank.png").convert_alpha()
quadrato5_rect=quadrato5.get_rect(topleft=(490,285))

quadrato6=pygame.image.load(r"C:\Users\ivano\Desktop\Giochi Fatti Da Me\Python\Tic Tac Toe\immagini\blank.png").convert_alpha()
quadrato6_rect=quadrato6.get_rect(topleft=(800,285))

quadrato7=pygame.image.load(r"C:\Users\ivano\Desktop\Giochi Fatti Da Me\Python\Tic Tac Toe\immagini\blank.png").convert_alpha()
quadrato7_rect=quadrato7.get_rect(topleft=(165,490))

quadrato8=pygame.image.load(r"C:\Users\ivano\Desktop\Giochi Fatti Da Me\Python\Tic Tac Toe\immagini\blank.png").convert_alpha()
quadrato8_rect=quadrato8.get_rect(topleft=(490,490))

quadrato9=pygame.image.load(r"C:\Users\ivano\Desktop\Giochi Fatti Da Me\Python\Tic Tac Toe\immagini\blank.png").convert_alpha()
quadrato9_rect=quadrato9.get_rect(topleft=(800,490))

pvcpu=pygame.image.load(r"C:\Users\ivano\Desktop\Giochi Fatti Da Me\Python\Tic Tac Toe\immagini\playervscpu.png").convert_alpha()
pvcpu_rect=pvcpu.get_rect(topleft=(375,300))

pvp=pygame.image.load(r"C:\Users\ivano\Desktop\Giochi Fatti Da Me\Python\Tic Tac Toe\immagini\pvp.png").convert_alpha()
pvp_rect=pvp.get_rect(topleft=(575,300))

screen.blit(pvcpu,pvcpu_rect)
screen.blit(pvp,pvp_rect)

game_active=False

spazi=[1,2,3,4,5,6,7,8,9]

turn=1

si1=False
si2=False
si3=False
si4=False
si5=False
si6=False
si7=False
si8=False
si9=False

vittoriacroce=False
vittoriacerchio=False
pareggio=False

sii1=False
sii2=False
sii3=False
sii4=False
sii5=False
sii6=False
sii7=False
sii8=False
sii9=False

siii1=False
siii2=False
siii3=False
siii4=False
siii5=False
siii6=False
siii7=False
siii8=False
siii9=False

blittati=False

inizio=True

p=False
cpu=False

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()

    if game_active:
        if blittati==False:
            screen.blit(griglia,(0,0))
            screen.blit(quadrato1,quadrato1_rect)
            screen.blit(quadrato2,quadrato2_rect)
            screen.blit(quadrato3,quadrato3_rect)
            screen.blit(quadrato4,quadrato4_rect)
            screen.blit(quadrato5,quadrato5_rect)
            screen.blit(quadrato6,quadrato6_rect)
            screen.blit(quadrato7,quadrato7_rect)
            screen.blit(quadrato8,quadrato8_rect)
            screen.blit(quadrato9,quadrato9_rect)
            blittati=True
        if cpu:
            if pygame.mouse.get_pressed()[0]:
                if turn==1:
                    mouse_pos=pygame.mouse.get_pos()
                    if quadrato1_rect.collidepoint(mouse_pos) and si1==False:
                        screen.blit(croce,quadrato1_rect)
                        si1=True
                        turn=0
                        if 1 in spazi:
                            spazi.remove(1)
                        siii1=True
                    else:
                        if quadrato2_rect.collidepoint(mouse_pos) and si2==False:
                            screen.blit(croce,quadrato2_rect)
                            si2=True
                            turn=0
                            if 2 in spazi:
                                spazi.remove(2)
                            siii2=True
                        else:
                            if quadrato3_rect.collidepoint(mouse_pos) and si3==False:
                                screen.blit(croce,quadrato3_rect)
                                si3=True
                                turn=0
                                if 3 in spazi:
                                    spazi.remove(3)
                                siii3=True
                            else:
                                if quadrato4_rect.collidepoint(mouse_pos) and si4==False:
                                    screen.blit(croce,quadrato4_rect)
                                    si4=True
                                    turn=0
                                    if 4 in spazi:
                                        spazi.remove(4)
                                    siii4=True
                                else:
                                    if quadrato5_rect.collidepoint(mouse_pos) and si5==False:
                                        screen.blit(croce,quadrato5_rect)
                                        si5=True
                                        turn=0
                                        if 5 in spazi:
                                            spazi.remove(5)
                                        siii5=True
                                    else:
                                        if quadrato6_rect.collidepoint(mouse_pos) and si6==False:
                                            screen.blit(croce,quadrato6_rect)
                                            si6=True
                                            turn=0
                                            if 6 in spazi:
                                                spazi.remove(6)
                                            siii6=True
                                        else:
                                            if quadrato7_rect.collidepoint(mouse_pos) and si7==False:
                                                screen.blit(croce,quadrato7_rect)
                                                si7=True
                                                turn=0
                                                if 7 in spazi:
                                                    spazi.remove(7)
                                                siii7=True
                                            else:
                                                if quadrato8_rect.collidepoint(mouse_pos) and si8==False:
                                                    screen.blit(croce,quadrato8_rect)
                                                    si8=True
                                                    turn=0
                                                    if 8 in spazi:
                                                        spazi.remove(8)
                                                    siii8=True
                                                else:
                                                    if quadrato9_rect.collidepoint(mouse_pos) and si9==False:
                                                        screen.blit(croce,quadrato9_rect)
                                                        si9=True
                                                        turn=0
                                                        if 9 in spazi:
                                                            spazi.remove(9)
                                                        siii9=True

            if turn==0:
                if len(spazi)>0:
                    x=random.choice(spazi)
                    if x==1 and si1==False:
                        screen.blit(cerchio,quadrato1_rect)
                        si1=True
                        turn=1
                        if 1 in spazi:
                            spazi.remove(1)
                        sii1=True
                    else:
                        if x==2 and si2==False:
                            screen.blit(cerchio,quadrato2_rect)
                            si2=True
                            turn=1
                            if 2 in spazi:
                                spazi.remove(2)
                            sii2=True
                        else:
                            if x==3 and si3==False:
                                screen.blit(cerchio,quadrato3_rect)
                                si3=True
                                turn=1
                                if 3 in spazi:
                                    spazi.remove(3)
                                sii3=True
                            else:
                                if x==4 and si4==False:
                                    screen.blit(cerchio,quadrato4_rect)
                                    si4=True
                                    turn=1
                                    if 4 in spazi:
                                        spazi.remove(4)
                                    sii4=True
                                else:
                                    if x==5 and si5==False:
                                        screen.blit(cerchio,quadrato5_rect)
                                        si5=True
                                        turn=1
                                        if 5 in spazi:
                                            spazi.remove(5)
                                        sii5=True
                                    else:
                                        if x==6 and si6==False:
                                            screen.blit(cerchio,quadrato6_rect)
                                            si6=True
                                            turn=1
                                            if 6 in spazi:
                                                spazi.remove(6)
                                            sii6=True
                                        else:
                                            if x==7 and si7==False:
                                                screen.blit(cerchio,quadrato7_rect)
                                                si7=True
                                                turn=1
                                                if 7 in spazi:
                                                    spazi.remove(7)
                                                sii7=True
                                            else:
                                                if x==8 and si8==False:
                                                    screen.blit(cerchio,quadrato8_rect)
                                                    si8=True
                                                    turn=1
                                                    if 8 in spazi:
                                                        spazi.remove(8)
                                                    sii8=True
                                                else:
                                                    if x==9 and si9==False:
                                                        screen.blit(cerchio,quadrato9_rect)
                                                        si9=True
                                                        turn=1
                                                        if 9 in spazi:
                                                            spazi.remove(9)
                                                        sii9=True
        else:
            if p:
                if pygame.mouse.get_pressed()[0]:
                    if turn==1:
                        mouse_pos=pygame.mouse.get_pos()
                        if quadrato1_rect.collidepoint(mouse_pos) and si1==False:
                            screen.blit(croce,quadrato1_rect)
                            turn=0
                            if 1 in spazi:
                                spazi.remove(1)
                            siii1=True
                        else:
                            if quadrato2_rect.collidepoint(mouse_pos) and si2==False:
                                screen.blit(croce,quadrato2_rect)
                                turn=0
                                if 2 in spazi:
                                    spazi.remove(2)
                                siii2=True
                            else:
                                if quadrato3_rect.collidepoint(mouse_pos) and si3==False:
                                    screen.blit(croce,quadrato3_rect)
                                    turn=0
                                    if 3 in spazi:
                                        spazi.remove(3)
                                    siii3=True
                                else:
                                    if quadrato4_rect.collidepoint(mouse_pos) and si4==False:
                                        screen.blit(croce,quadrato4_rect)
                                        turn=0
                                        if 4 in spazi:
                                            spazi.remove(4)
                                        siii4=True
                                    else:
                                        if quadrato5_rect.collidepoint(mouse_pos) and si5==False:
                                            screen.blit(croce,quadrato5_rect)
                                            turn=0
                                            if 5 in spazi:
                                                spazi.remove(5)
                                            siii5=True
                                        else:
                                            if quadrato6_rect.collidepoint(mouse_pos) and si6==False:
                                                screen.blit(croce,quadrato6_rect)
                                                turn=0
                                                if 6 in spazi:
                                                    spazi.remove(6)
                                                siii6=True
                                            else:
                                                if quadrato7_rect.collidepoint(mouse_pos) and si7==False:
                                                    screen.blit(croce,quadrato7_rect)
                                                    turn=0
                                                    if 7 in spazi:
                                                        spazi.remove(7)
                                                    siii7=True
                                                else:
                                                    if quadrato8_rect.collidepoint(mouse_pos) and si8==False:
                                                        screen.blit(croce,quadrato8_rect)
                                                        turn=0
                                                        if 8 in spazi:
                                                            spazi.remove(8)
                                                        siii8=True
                                                    else:
                                                        if quadrato9_rect.collidepoint(mouse_pos) and si9==False:
                                                            screen.blit(croce,quadrato9_rect)
                                                            turn=0
                                                            if 9 in spazi:
                                                                spazi.remove(9)
                                                            siii9=True
                else:
                    keys=pygame.key.get_pressed()
                    if keys[pygame.K_t] and 1 in spazi:
                        screen.blit(croce,quadrato1_rect)
                        turn=0
                        if 1 in spazi:
                            spazi.remove(1)
                        siii1=True
                    else:
                        if keys[pygame.K_y] and 2 in spazi:
                            screen.blit(croce,quadrato2_rect)
                            turn=0
                            if 2 in spazi:
                                spazi.remove(2)
                            siii2=True
                        else:
                            if keys[pygame.K_u] and 3 in spazi:
                                screen.blit(croce,quadrato3_rect)
                                turn=0
                                if 3 in spazi:
                                    spazi.remove(3)
                                siii3=True
                            else:
                                if keys[pygame.K_g] and 4 in spazi:
                                    screen.blit(croce,quadrato4_rect)
                                    turn=0
                                    if 4 in spazi:
                                        spazi.remove(4)
                                    siii4=True
                                else:
                                    if keys[pygame.K_h] and 5 in spazi:
                                        screen.blit(croce,quadrato5_rect)
                                        turn=0
                                        if 5 in spazi:
                                            spazi.remove(5)
                                        siii5=True
                                    else:
                                        if keys[pygame.K_j] and 6 in spazi:
                                            screen.blit(croce,quadrato6_rect)
                                            turn=0
                                            if 6 in spazi:
                                                spazi.remove(6)
                                            siii6=True
                                        else:
                                            if keys[pygame.K_b] and 7 in spazi:
                                                screen.blit(croce,quadrato7_rect)
                                                turn=0
                                                if 7 in spazi:
                                                    spazi.remove(7)
                                                siii7=True
                                            else:
                                                if keys[pygame.K_n] and 8 in spazi:
                                                    screen.blit(croce,quadrato8_rect)
                                                    turn=0
                                                    if 8 in spazi:
                                                        spazi.remove(8)
                                                    siii8=True
                                                else:
                                                    if keys[pygame.K_m] and 9 in spazi:
                                                        screen.blit(croce,quadrato9_rect)
                                                        turn=0
                                                        if 9 in spazi:
                                                            spazi.remove(9)
                                                        siii9=True

                    if turn==0:
                        if pygame.mouse.get_pressed()[0]:
                            keys=pygame.key.get_pressed()
                            mouse_pos=pygame.mouse.get_pos()
                            if quadrato1_rect.collidepoint(mouse_pos) and si1==False:
                                screen.blit(cerchio,quadrato1_rect)
                                turn=1
                                if 1 in spazi:
                                    spazi.remove(1)
                                siii1=True
                            else:
                                if quadrato2_rect.collidepoint(mouse_pos) and si2==False:
                                    screen.blit(cerchio,quadrato2_rect)
                                    turn=1
                                    if 2 in spazi:
                                        spazi.remove(2)
                                    siii2=True
                                else:
                                    if quadrato3_rect.collidepoint(mouse_pos) and si3==False:
                                        screen.blit(cerchio,quadrato3_rect)
                                        turn=1
                                        if 3 in spazi:
                                            spazi.remove(3)
                                        siii3=True
                                    else:
                                        if quadrato4_rect.collidepoint(mouse_pos) and si4==False:
                                            screen.blit(cerchio,quadrato4_rect)
                                            turn=1
                                            if 4 in spazi:
                                                spazi.remove(4)
                                            siii4=True
                                        else:
                                            if quadrato5_rect.collidepoint(mouse_pos) and si5==False:
                                                screen.blit(cerchio,quadrato5_rect)
                                                turn=1
                                                if 5 in spazi:
                                                    spazi.remove(5)
                                                siii5=True
                                            else:
                                                if quadrato6_rect.collidepoint(mouse_pos) and si6==False:
                                                    screen.blit(cerchio,quadrato6_rect)
                                                    turn=1
                                                    if 6 in spazi:
                                                        spazi.remove(6)
                                                    siii6=True
                                                else:
                                                    if quadrato7_rect.collidepoint(mouse_pos) and si7==False:
                                                        screen.blit(cerchio,quadrato7_rect)
                                                        turn=1
                                                        if 7 in spazi:
                                                            spazi.remove(7)
                                                        siii7=True
                                                    else:
                                                        if quadrato8_rect.collidepoint(mouse_pos) and si8==False:
                                                            screen.blit(cerchio,quadrato8_rect)
                                                            turn=1
                                                            if 8 in spazi:
                                                                spazi.remove(8)
                                                            siii8=True
                                                        else:
                                                            if quadrato9_rect.collidepoint(mouse_pos) and si9==False:
                                                                screen.blit(cerchio,quadrato9_rect)
                                                                turn=1
                                                                if 9 in spazi:
                                                                    spazi.remove(9)
                                                                siii9=True
                        else:
                            keys=pygame.key.get_pressed()
                            if keys[pygame.K_q] and 1 in spazi:
                                screen.blit(cerchio,quadrato1_rect)
                                turn=1
                                if 1 in spazi:
                                    spazi.remove(1)
                                sii1=True
                            else:
                                if keys[pygame.K_w] and 2 in spazi:
                                    screen.blit(cerchio,quadrato2_rect)
                                    turn=1
                                    if 2 in spazi:
                                        spazi.remove(2)
                                    sii2=True
                                else:
                                    if keys[pygame.K_e] and 3 in spazi:
                                        screen.blit(cerchio,quadrato3_rect)
                                        turn=1
                                        if 3 in spazi:
                                            spazi.remove(3)
                                        sii3=True
                                    else:
                                        if keys[pygame.K_a] and 4 in spazi:
                                            screen.blit(cerchio,quadrato4_rect)
                                            turn=1
                                            if 4 in spazi:
                                                spazi.remove(4)
                                            sii4=True
                                        else:
                                            if keys[pygame.K_s] and 5 in spazi:
                                                screen.blit(cerchio,quadrato5_rect)
                                                turn=1
                                                if 5 in spazi:
                                                    spazi.remove(5)
                                                sii5=True
                                            else:
                                                if keys[pygame.K_d] and 6 in spazi:
                                                    screen.blit(cerchio,quadrato6_rect)
                                                    turn=1
                                                    if 6 in spazi:
                                                        spazi.remove(6)
                                                    sii6=True
                                                else:
                                                    if keys[pygame.K_z] and 7 in spazi:
                                                        screen.blit(cerchio,quadrato7_rect)
                                                        turn=1
                                                        if 7 in spazi:
                                                            spazi.remove(7)
                                                        sii7=True
                                                    else:
                                                        if keys[pygame.K_x] and 8 in spazi:
                                                            screen.blit(cerchio,quadrato8_rect)
                                                            turn=1
                                                            if 8 in spazi:
                                                                spazi.remove(8)
                                                            sii8=True
                                                        else:
                                                            if keys[pygame.K_c] and 9 in spazi:
                                                                screen.blit(cerchio,quadrato9_rect)
                                                                turn=1
                                                                if 9 in spazi:
                                                                    spazi.remove(9)
                                                                sii9=True

        if siii1 and siii2 and siii3:
            vittoriacroce=True
        else:
            if siii4 and siii5 and siii6:
                vittoriacroce=True
            else:
                if siii7 and siii8 and siii9:
                  vittoriacroce=True
                else:
                    if siii1 and siii4 and siii7:
                       vittoriacroce=True
                    else:
                        if siii2 and siii5 and siii8:
                            vittoriacroce=True
                        else:
                            if siii3 and siii6 and siii9:
                                vittoriacroce=True
                            else:
                                if siii1 and siii5 and siii9:
                                    vittoriacroce=True
                                else:
                                    if siii3 and siii5 and siii7:
                                        vittoriacroce=True
                                    else:
                                        if sii1 and sii2 and sii3:
                                            vittoriacerchio=True
                                        else:
                                            if sii4 and sii5 and sii6:
                                                vittoriacerchio=True
                                            else:
                                                if sii7 and sii8 and sii9:
                                                    vittoriacerchio=True
                                                else:
                                                    if sii1 and sii4 and sii7:
                                                        vittoriacerchio=True
                                                    else:
                                                        if sii2 and sii5 and sii8:
                                                            vittoriacerchio=True
                                                        else:
                                                            if sii3 and sii6 and sii9:
                                                                vittoriacerchio=True
                                                            else:
                                                                if sii1 and sii5 and sii9:
                                                                    vittoriacerchio=True
                                                                else:
                                                                    if sii3 and sii5 and sii7:
                                                                        vittoriacerchio=True

        inizio=False

        if len(spazi)==0:
            pareggio=True

        if vittoriacerchio or vittoriacroce or pareggio:
            game_active=False

    if not game_active:
        if inizio:
            screen.fill("Black",None,0)
            screen.blit(pvp,pvp_rect)
            screen.blit(pvcpu,pvcpu_rect)
            mouse_pos=pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0]:
                if pvcpu_rect.collidepoint(mouse_pos):
                    game_active=True
                    cpu=True
                else:
                    if pvp_rect.collidepoint(mouse_pos):
                        game_active=True
                        p=True

        if vittoriacroce:
            screen.blit(pygame.image.load(r"C:\Users\ivano\Desktop\Giochi Fatti Da Me\Python\Tic Tac Toe\immagini\cross_win.png").convert_alpha(),(0,0))
        else:
            if vittoriacerchio:
                screen.blit(pygame.image.load(r"C:\Users\ivano\Desktop\Giochi Fatti Da Me\Python\Tic Tac Toe\immagini\circle_win.png").convert_alpha(),(0,0))
            else:
                if pareggio:
                    screen.blit(pygame.image.load(r"C:\Users\ivano\Desktop\Giochi Fatti Da Me\Python\Tic Tac Toe\immagini\tie.png").convert_alpha(),(0,0))

    pygame.display.update()
    clock.tick(60)
