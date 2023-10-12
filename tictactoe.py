import pygame
import random

width = 300
height = 300

darkblue = 14, 34, 207
violet = 166, 12, 237
cyan = 12, 237, 222
yellow = 242, 207, 29

gameover = False

field = [['','',''],['','',''],['','','']]

fps = 30

pygame.init()

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Крестики Нолики')

run = True

clock = pygame.time.Clock()

def grid():
    pygame.draw.line(screen,yellow,(100,0),(100,300),3)
    pygame.draw.line(screen,yellow,(200,0),(200,300),3)
    pygame.draw.line(screen,yellow,(0,100),(300,100),3)
    pygame.draw.line(screen,yellow,(0,200),(300,200),3)

def tictac():
    for i in range(3):
        for j in range(3):
            if field[i][j] == '0':
                pygame.draw.circle(screen,darkblue,(j*100+50, i*100+50), 50, 3 )
            if field[i][j] == 'x':
                pygame.draw.line(screen,darkblue,(j*100+5, i*100+5),(j*100+95,i*100+95), 3 )
                pygame.draw.line(screen,darkblue,(j*100+95, i*100+5),(j*100+5,i*100+95), 3 )

def wincheck(symbol):
    flag_win = False
    global pwin
    for line in field:
        if line.count(symbol) == 3:
            flag_win = True
            pwin = [[0,field.index(line)],[1,field.index(line)],[2,field.index(line)]]
    for i in range(3):
        if field[0][i] == field[1][i] == field[2][i] == symbol:
            flag_win = True
            pwin = [[i,0],[i,1],[i,2]]
    if field[0][0] == field[1][1] == field[2][2] == symbol:
        flag_win = True
        pwin = [[0,0],[1,1],[2,2]]
    if field[2][0] == field[1][1] == field[0][2] == symbol:
        flag_win = True
        pwin = [[2,0],[1,1],[0,2]]
    return flag_win


while run:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and not gameover:
            pos = pygame.mouse.get_pos()
            if field[pos[1]//100][pos[0]//100] == '':
                field[pos[1]//100][pos[0]//100] = 'x'
                x = random.randint(0,2)
                y = random.randint(0,2)
                while field[x][y] != '':
                    x = random.randint(0,2)
                    y = random.randint(0,2)
                field[x][y] = '0'
            win = wincheck('x')
            lose = wincheck('0')
            draw = field[0].count('x')+field[0].count('0')+field[1].count('x')+field[1].count('0')+field[2].count('x')+field[2].count('0')
            if win or lose:
                gameover = True
                if win:
                    pygame.display.set_caption('Выйграл!')
                else:
                    pygame.display.set_caption('Проиграл!')
            elif draw == 8:
                pygame.display.set_caption('Ничья!')
    screen.fill(violet)
    if gameover:
        pygame.draw.rect(screen,cyan,(pwin[0][0]*100,pwin[0][1]*100, 100, 100))
        pygame.draw.rect(screen,cyan,(pwin[1][0]*100,pwin[1][1]*100, 100, 100))
        pygame.draw.rect(screen,cyan,(pwin[2][0]*100,pwin[2][1]*100, 100, 100))
    grid()
    tictac()
    pygame.display.flip()
pygame.quit()

