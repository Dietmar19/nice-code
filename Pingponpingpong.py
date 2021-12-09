# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 17:46:36 2021

@author: Dietmar
"""

import pygame
import random
import sys

x = 500   # Höhe des Fensters
y = 500   # Breite des Fensters

sbreite = 100  # Schlägerbreite
shoehe = 15    # Schlägerhöhe

sx  = 200  # oeres linkes eck x koordinate
sy = 450   # oeres linkes eck y koordinate

bx = int(x/2)  # koordinaten des Balles
by = int(y/2)  # koordinaten des Balles

brad = 15   # Radius des Balles

speed = 0 # Speed des Schlägers

bxspeed = 1  # damit sich deer Ball nach links und rechts bewegen kann
byspeed = -2  # damit sich deer Ball nach oben und unten bewegen kann

leben = 3  # Anzahl der Leben Todeszone

pygame.init()   # Initialiierung von pygame

screen = pygame.display.set_mode([x,y])
screen.fill((0,0,0))

pygame.draw.circle(screen, (255,255,0), (bx,by), brad, 0)# Erzeugung des Balles auf der Oberfläche - Farbe: gelb 
                                                         # übergabe der Koordinaten des Balles
                                                         # Übergabe Radius
                                                         # 0 - Ball ist ausgefüllt

pygame.draw.rect(screen, (255,40,0), (sx,sy,sbreite, shoehe),0)        # Erzeugung des Schlägers in rot
                                                                    # Koordinaten des Schläger
                                                                    # Höhe und Breite des Schlägers
                                                                    # 0 - Schläger ist ausgefüllt
                                                                    
pygame.display.flip()   # das wir den Ball und Schläger auf dem Screen sehen

def sblock():
    global speed
    if sx <= 0 or sx >= x-sbreite:    # falls des Schläger mit der wand kollidiert
        speed = 0                   # dann wird die geschwindkeit auf o gesetzt
        
def ballbewegung():    # methode ballbewegung
    global bx,by       # Position des Balles                         
    bx += byspeed
    by += byspeed
    
    
def reset():                                # reseten wenn gestorben
    global byspeed, bxspeed, leben, bx, by, sx, sy, speed
    sx = 200
    sy = 450
    
    bx = int(x/2)
    by = int(y/2)
    
    speed = 0
    bxspeed = random.randint(-2,2)       #Zufälligkeit , damit sich der Ball nicht immer gleich bewegt'
    if bxspeed = 0:
        bxspeed = 1
    
    byspeed = random.randint(-2,2)      #random , damit sich der Ball nicht immer gleich bewegt'
    
    if byspeed = 0:
        byspeed = 2
    screen.fill((0,0,0))    
    pygame.draw.circle(screen, (255,255,0), (bx,by), brad, 0)
    pygame.draw.rect(screen, (255,40,0), (sx,sy,sbreite, shoehe),0)
    pygame.display.flip() 
    pygame.time.wait(1000)
    
def ballblock():                       # wann, wo und wie der Ball abprallen soll'
    global byspeed, bxspeed, leben
    if by-brad <= 0:
        byspeed *=-1                   # falls byspeed wird er negativ bzw umgekehrt -- kehrt sich Bew-Richtung um
    if bx-brad <= 0:
        bxspeed *= -1
    if bx+brad >= x:
        bxspeed *0 -1
    if by >= 435 and by <= 440:
        if bx >= sx-15  and bx <= sx+sbreite+15:  
            byspeed *= -1
        else:
            leben -= 1
            reset()
            
def sbewegung():    # schlägerbewegung'
    global sx
    sx += speed   
    
while leben>0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()     # bei spiel quittieren spiel verlassen
        if event.type == pygame.KEYDOWN:            # tastenbetätigung
            if event.key == pygame.K_LEFT:           # linkeTaste
                speed = -2
            if event.key == pygame.K_RIGHT:          # rechte Taste
                speed = 2
    screen.fill((0,0,0)) 
    sbewegung()
    sblock()
    pygame.draw.rect(screen, (255,40,0), (sx,sy,sbreite, shoehe),0)
    ballbewegung()
    ballblock()
    pygame.draw.circle(screen, (255,255,0), (bx,by), brad, 0)
    pygame.display.flip(()                        # sichtbar nachen auf dem Bildschirm         
    pygame.time.wait(5)                          # Ball verlangsamen     
                
print("Du hast verloren")
                
                
    
 
