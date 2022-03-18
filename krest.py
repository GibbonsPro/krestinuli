import pygame as pg
import numpy as np
from time import sleep


def checkwin(map, x, y, player):
    leftc = 0
    rightc = 0
    upc = 0
    downc = 0
    right_diagonal_upc = 0
    right_diagonal_downc = 0
    left_diagonal_upc = 0
    left_diagonal_downc = 0
    i = 1
    while map[x-i][y] == player:
        leftc += 1
        i+=1
    i = 1
    while map[x+i][y] == player:
        rightc += 1
        i+=1   
    i = 1
    while map[x][y-i] == player:
        downc += 1
        i+=1   
    i = 1
    while map[x][y+i] == player:
        upc += 1
        i+=1
    i = 1
    
    while map[x-i][y-i] == player:
        left_diagonal_upc += 1
        i+=1
    i = 1
    while map[x+i][y+i] == player:
        left_diagonal_downc += 1
        i+=1   
    i = 1
    while map[x+i][y-i] == player:
        right_diagonal_upc += 1
        i+=1   
    i = 1
    while map[x-i][y+i] == player:
        right_diagonal_downc += 1
        i+=1
    if leftc+rightc>=4 or upc+downc>=4 or right_diagonal_downc+right_diagonal_upc>=4 \
            or left_diagonal_downc+left_diagonal_upc>=4:
        dis.blit(text, [250,250])
        return True
    return False


pg.init()

dis = pg.display.set_mode((800, 800))

white = (255, 255, 255)
red = (225, 0, 50)
green = (0, 225, 0)
blue = (0, 0, 225)
black = (0, 0, 0)

font = pg.font.Font(None, 75)
text = font.render("Ура! Победа...",True, black)

dis.fill(white)

def start_game():
    global map, gameover, counter, dis
    dis.fill(white)
    map = np.zeros((40, 40))
    gameover = False
    counter = 0

    for x in range(0, 800, 20):
        pg.draw.line(dis, black, [x, 0], [x, 800])
        for y in range(0, 800, 20):
            pg.draw.line(dis, black, [800, y], [0, y])

map = np.zeros((40, 40))
gameover = False
counter = 0

start_game()

while not gameover:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            gameover=True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_r and gameover == True:
                start_game()
            elif event.key == pg.K_q:
                gameover = True
        i = 0
        
        if event.type == pg.MOUSEBUTTONDOWN and counter == 0:
            if event.button == 1 and map[event.pos[0]//20][event.pos[1]//20] != 1 and map[event.pos[0]//20][event.pos[1]//20] != 2:
                pg.draw.line(
                    dis, red, [event.pos[0] - event.pos[0] % 20, event.pos[1] - event.pos[1] % 20],
                     [event.pos[0] - event.pos[0] % 20 + 20, event.pos[1] - event.pos[1] % 20 + 20], 3)
                pg.draw.line(
                    dis, red, [event.pos[0] - event.pos[0] % 20, event.pos[1] - event.pos[1] % 20 + 20],
                     [event.pos[0] - event.pos[0] % 20 + 20, event.pos[1] - event.pos[1] % 20], 3)
                map[event.pos[0]//20][event.pos[1]//20] = 1
                
                pg.display.update()
                counter = 1
                checkwin(map, event.pos[0]//20, event.pos[1]//20, 1)
            
        elif event.type == pg.MOUSEBUTTONDOWN and counter == 1:
            if event.button == 1 and map[event.pos[0]//20][event.pos[1]//20] != 1 and map[event.pos[0]//20][event.pos[1]//20] != 2:
                pg.draw.circle(dis, blue, (event.pos[0] - event.pos[0] % 20 + 10,
                 event.pos[1] - event.pos[1] % 20 + 10), 10, 2)
                map[event.pos[0]//20][event.pos[1]//20] = 2
                
                pg.display.update() 
                counter = 0
                checkwin(map, event.pos[0]//20, event.pos[1]//20, 2)
        

    pg.display.update()