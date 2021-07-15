import pygame
import os
import numpy as np
import random
import math

##os.environ['SDL_VIDEODRIVER'] = 'directx'

pygame.mixer.pre_init(44100, 16, 8, 4096)
pygame.init()
dwidth = 1280
dheight = 720
gameDisplay = pygame.display.set_mode((dwidth, dheight))
pygame.display.set_caption('Escape From the Soviet Union')
clock = pygame.time.Clock()
bgColor = (145, 180, 235)

turn = 1
visibility = 100
difficulty = None

toggleFreeTile = False
toggleCity = False
toggleRail = False

otr = False
otrUsed = False
otrTurn = None

ev = False
evUsed = False
evTurn = None


boardArray = np.ndarray((20,24), int)

##Free Territory

for i in range(0,20,1):
    for j in range(0,23,1):
        boardArray[i][j] = 0

for i in range(4,9,1):
    boardArray[0][i] = 1

for i in range(11,14,1):
    boardArray[0][i] = 1

for i in range(4,9,1):
    boardArray[1][i] = 1

for i in range(11,13,1):
    boardArray[1][i] = 1

for i in range(4,10,1):
    boardArray[2][i] = 1

for i in range(6,9,1):
    boardArray[3][i] = 1

boardArray[4][5] = 1

for i in range(7,9,1):
    boardArray[4][i] = 1

for i in range(5,8,1):
    boardArray[5][i] = 1

boardArray[6][4] = 1
boardArray[6][5] = 1

for i in range(3,5,1):
    boardArray[7][i] = 1

for i in range(1,5,1):
    boardArray[8][i] = 1

for i in range(0,5,1):
    boardArray[9][i] = 1

for i in range(0,6,1):
    boardArray[10][i] = 1

for i in range(0,6,1):
    boardArray[11][i] = 1

for i in range(0,8,1):
    boardArray[12][i] = 1

for i in range(0,6,1):
    boardArray[13][i] = 1

for i in range(0,6,1):
    boardArray[14][i] = 1

boardArray[15][1] = 1

for i in range(4,6,1):
    boardArray[15][i] = 1

for i in range(4,6,1):
    boardArray[16][i] = 1

for i in range(5,8,1):
    boardArray[17][i] = 1

for i in range(6,9,1):
    boardArray[18][i] = 1

boardArray[19][7] = 1

for i in range(22,24,1):
    boardArray[16][i] = 1

for i in range(14,24,1):
    boardArray[17][i] = 1

for i in range(11,24,1):
    boardArray[18][i] = 1

for i in range(10,12,1):
    boardArray[19][i] = 1

for i in range(14,24,1):
    boardArray[19][i] = 1

##Cities

boardArray[2][14] = 2
boardArray[4][12] = 2
boardArray[5][16] = 2
boardArray[7][13] = 2
boardArray[8][6] = 2
boardArray[9][10] = 2
boardArray[10][7] = 2
boardArray[10][15] = 2
boardArray[12][9] = 2
boardArray[12][20] = 2
boardArray[14][9] = 2
boardArray[15][13] = 2
boardArray[17][11] = 2

##Railways

for i in range(12,16,1):
    boardArray[5][i] = 3

for i in range(6,10,1):
    boardArray[i][16] = 3

boardArray[10][16] = 3
boardArray[11][17] = 3
boardArray[11][18] = 3
boardArray[12][19] = 3

boardArray[11][15] = 3
boardArray[12][15] = 3
boardArray[12][14] = 3
boardArray[13][14] = 3
boardArray[14][13] = 3

for i in range(15, 18, 1):
    boardArray[i][12] = 3

boardArray[15][11] = 3
boardArray[14][10] = 3

boardArray[13][9] = 3

boardArray[11][9] = 3
boardArray[10][10] = 3

boardArray[9][9] = 3
boardArray[10][8] = 3

##Major Railways

boardArray[4][16] = 4
boardArray[4][15] = 4
boardArray[3][15] = 4
boardArray[3][14] = 4

boardArray[6][16] = 6
boardArray[6][15] = 4
boardArray[7][14] = 4

boardArray[8][12] = 4
boardArray[8][11] = 4

boardArray[9][9] = 6
boardArray[8][9] = 4
boardArray[8][8] = 4
boardArray[8][7] = 4


mapng = pygame.transform.smoothscale(pygame.image.load('files/sovmapFNoGrid.png'),(800,615))
mapg = pygame.transform.smoothscale(pygame.image.load('files/sovmapFGrid.png'),(800,615))
rect = pygame.transform.smoothscale(pygame.image.load('files/rect.png'),(850,675))
spy = pygame.transform.smoothscale(pygame.image.load('files/spy2.png'),(20,20))
kgb = pygame.transform.smoothscale(pygame.image.load('files/kgb2.png'),(20,20))
greenCircle = pygame.transform.smoothscale(pygame.image.load('files/greenCircle.png'),(23,23))
whiteCircle = pygame.transform.smoothscale(pygame.image.load('files/whiteCircle.png'),(23,23))
blueCircle = pygame.transform.smoothscale(pygame.image.load('files/blueCircle.png'),(23,23))
yellowCircle = pygame.transform.smoothscale(pygame.image.load('files/yellowCircle.png'),(23,23))
titleScreen = pygame.transform.smoothscale(pygame.image.load('files/sovtitle.png'),(1280,720))
lsScreen = pygame.transform.smoothscale(pygame.image.load('files/levelSelectScreen.png'),(1280,720))
successScreen = pygame.transform.smoothscale(pygame.image.load('files/successScreen.png'),(1280,720))
deathScreen = pygame.transform.smoothscale(pygame.image.load('files/deathScreen.png'),(1280,720))
enhancedVision = pygame.image.load('files/enhancedVision.png')
offTheRadar = pygame.image.load('files/offTheRadar.png')
evActive = pygame.image.load('files/evActive.png')
otrActive = pygame.image.load('files/otrActive.png')
sidebar = pygame.image.load('files/sovbar2.png')
rules1 = pygame.transform.smoothscale(pygame.image.load('files/rules1.png'),(1280,720))
rules2 = pygame.transform.smoothscale(pygame.image.load('files/rules2.png'),(1280,720))

saSound = pygame.mixer.Sound('files/saSound.wav')
saSound.set_volume(0.5)
clickSound = pygame.mixer.Sound('files/clickSound.wav')
clickSound.set_volume(1.2)
deathSound = pygame.mixer.Sound('files/deathSound.wav')
deathSound.set_volume(0.5)
winSound = pygame.mixer.Sound('files/winSound.wav')
winSound.set_volume(0.4)
nextTurnSound = pygame.mixer.Sound('files/nextTurnSound.wav')
nextTurnSound.set_volume(0.3)

hitman = pygame.mixer.Sound('files/hitman.wav')
hitman.set_volume(0.12)
detective = pygame.mixer.Sound('files/detective.wav')
detective.set_volume(0.12)

musicArray = [hitman, detective]

kgbAgents = []

black = (0,0,0)
white = (255, 255, 255)

border = [(0,14),(1,14),(1,13),(2,13),(2,12),(3,12),(3,11),(3,10),(4,10),(4,9),(5,9),(6,9),(6,8),(6,7),(7,7),(7,6),(7,5),(8,5),(9,5),(9,6),(10,6),(11,6),(11,7),(11,8),(12,8),(13,8),(13,7),(14,7),(15,7),(16,7),(16,8),(17,8),(17,9),(17,10),(17,11),(17,12),(17,13),(16,13),(16,14),(16,15),(16,16)]
for i in range(16,24,1):
    border.append((15, i))

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_display(text, n, m, size, font, color):
    font = pygame.font.SysFont(font, size)
    ##largeText = pygame.font.Font('freesansbold.ttf',size)
    TextSurf, TextRect = text_objects(text, font, color)
    TextRect.center = (int(n)),(int(m))
    gameDisplay.blit(TextSurf, TextRect)

def place(a,x,y):
    gameDisplay.blit(a, (x,y))

def centralPlace(a,cx,cy,w,h):
    gameDisplay.blit(a, (cx-(w/2), cy-(h/2)))

def gridToCoords(row, col):
    y = 67.4 + 30.75*row
    x = 84.7 + 33.33*col
    return (x,y)

def coordsToGrid(x, y):
    row = round((y - 67.4)/30.75)
    col = round((x - 84.7)/33.33)
    return (row, col)

def freeTile(r, c):
    free = True
    for i in kgbAgents:
        if i.getRow() == r and i.getColumn() == c:
            free = False
    return free

class Pspy:
    def __init__(self, row, column):
        self.row = row
        self.column = column
    def getRow(self):
        return self.row
    def getColumn(self):
        return self.column

class Ckgb:
    def __init__(self, type, row, column):
        self.type = type
        self.row = row
        self.column = column
    def getType(self):
        return self.type
    def getRow(self):
        return self.row
    def getColumn(self):
        return self.column
    def move(self):
        global border
        moveList = []
        if self.type == 1:
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    if (self.getRow() + i) >= 0 and (self.getRow() + i) <= 19 and (self.getColumn() + j) >= 0 and (self.getColumn() + j) <= 23 and not(i == 0 and j == 0):
                        if boardArray[self.getRow()+i][self.getColumn()+j] != 1:
                            if freeTile(self.getRow()+i, self.getColumn()+j):
                                moveList.append((self.getRow() + i, self.getColumn() + j))
            if len(moveList) > 0:
                r = random.random()
                s = math.floor(r*len(moveList))
                t = moveList[s]
                self.row = t[0]
                self.column = t[1]
                
        if self.type == 2:
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    if (self.getRow() + i) >= 0 and (self.getRow() + i) <= 19 and (self.getColumn() + j) >= 0 and (self.getColumn() + j) <= 23 and not(i == 0 and j == 0):
                        if boardArray[self.getRow()+i][self.getColumn()+j] == 3 or boardArray[self.getRow()+i][self.getColumn()+j] == 4:
                            if freeTile(self.getRow()+i, self.getColumn()+j):
                                moveList.append((self.getRow() + i, self.getColumn() + j))
            if len(moveList) > 0:
                r = random.random()
                s = math.floor(r*len(moveList))
                t = moveList[s]
                self.row = t[0]
                self.column = t[1]

        if self.type == 3:
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    if (self.getRow() + i) >= 0 and (self.getRow() + i) <= 19 and (self.getColumn() + j) >= 0 and (self.getColumn() + j) <= 23 and not(i == 0 and j == 0):
                        if boardArray[self.getRow()+i][self.getColumn()+j] != 1 and abs(player.getRow() - (self.getRow() + i)) <= abs(player.getRow() - self.getRow()) and abs(player.getColumn() - (self.getColumn() + j)) <= abs(player.getColumn() - self.getColumn()):
                            if freeTile(self.getRow()+i, self.getColumn()+j):
                                moveList.append((self.getRow() + i, self.getColumn() + j))
            if len(moveList) > 0:
                r = random.random()
                s = math.floor(r*len(moveList))
                t = moveList[s]
                self.row = t[0]
                self.column = t[1]

        if self.type == 4:
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    if (self.getRow() + i) >= 0 and (self.getRow() + i) <= 19 and (self.getColumn() + j) >= 0 and (self.getColumn() + j) <= 23 and not(i == 0 and j == 0):
                        if boardArray[self.getRow()+i][self.getColumn()+j] != 1 and (self.getRow()+i, self.getColumn()+j) in border:
                            if freeTile(self.getRow()+i, self.getColumn()+j):
                                moveList.append((self.getRow() + i, self.getColumn() + j))
            if len(moveList) > 0:
                r = random.random()
                s = math.floor(r*len(moveList))
                t = moveList[s]
                self.row = t[0]
                self.column = t[1]

player = Pspy(5,16)

def titleLoop():
    finished = False
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                finished = True
                
        gameDisplay.fill(bgColor)
        place(titleScreen, 0, 0)
        pygame.display.update()
        clock.tick(60)


def levelSelect():
    start = False
    while not start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                if y >= 343 and y <= 448:
                    if x >= 245 and x <= 376:
                        rulesLoop()
                        gameLoop('Easy')
                    elif x >= 477 and x <= 608:
                        rulesLoop()
                        gameLoop('Medium')
                    elif x >= 709 and x <= 840:
                        rulesLoop()
                        gameLoop('Hard')
                    elif x >= 941 and x <= 1072:
                        rulesLoop()
                        gameLoop('Death')
                
        if not pygame.mixer.Channel(7).get_busy():
            pygame.mixer.Channel(7).play(musicArray[int(random.random()*len(musicArray))])
        gameDisplay.fill(bgColor)
        place(lsScreen, 0, 0)
        message_display("Press Q to Quit Game", 60, 700, 10, 'times new roman', white)
        pygame.display.update()
        clock.tick(60)

def rulesLoop():
    start1 = False
    while not start1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                start1 = True
                
        if not pygame.mixer.Channel(7).get_busy():
            pygame.mixer.Channel(7).play(musicArray[int(random.random()*len(musicArray))])
        gameDisplay.fill(bgColor)
        place(rules1, 0, 0)
        pygame.display.update()
        clock.tick(60)
    start2 = False
    while not start2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                start2 = True
                
        if not pygame.mixer.Channel(7).get_busy():
            pygame.mixer.Channel(7).play(musicArray[int(random.random()*len(musicArray))])
        gameDisplay.fill(bgColor)
        place(rules2, 0, 0)
        pygame.display.update()
        clock.tick(60)
        

def gameLoop(diff):
    global turn, kgbAgents, border, visibility, player, difficulty, toggleFreeTile, toggleCity, toggleRail, otr, otrUsed, otrTurn, ev, evUsed, evTurn
    debug = False

    difficulty = diff
    
    finished = False
    won = False
    mp = 6
    
    toggleFreeTile = False
    toggleCity = False
    toggleRail = False

    otr = False
    if difficulty == 'Easy' or difficulty == 'Medium':
        otrUsed = False
    else:
        otrUsed = True
    otrTurn = None

    ev = False
    evUsed = False
    evTurn = None
    
    turn = 1
    keyHeld = False
    kgbAgents = []
    player = Pspy(5,16)


    if difficulty == 'Easy' or difficulty == 'Medium':
        for i in range(0,20,1):
            for j in range(7,23,1):
                if (abs(5 - i) > 2 or abs(16 - j) > 2) and boardArray[i][j] != 1 and freeTile(i, j):
                    r = random.random()
                    if i >= 7 and i <= 17 and j >= 7 and j <= 14:
                        if r < 0.05:
                            kgbAgents.append(Ckgb(1,i,j))
                    elif i >= 0 and i <= 5 and j >= 9 and j <= 15:
                        if r < 0.13:
                            kgbAgents.append(Ckgb(1,i,j))
                    else:
                        if r < 0.08:
                            kgbAgents.append(Ckgb(1,i,j))

        for i in range(0,20,1):
            for j in range(7,23,1):
                if (abs(5 - i) > 2 or abs(16 - j) > 2) and freeTile(i, j):
                    r = random.random()
                    if boardArray[i][j] == 3:
                        if r < 0.06:
                            kgbAgents.append(Ckgb(2, i, j))
                    elif boardArray[i][j] == 4:
                        if r < 0.13:
                            kgbAgents.append(Ckgb(2, i, j))

        for i in range(0,20,1):
            for j in range(7,23,1):
                if (abs(5 - i) > 2 or abs(16 - j) > 2) and freeTile(i, j) and boardArray[i][j] != 1:
                    r = random.random()
                    if r < 0.04:
                        kgbAgents.append(Ckgb(3,i,j))

        for i in border:
            if freeTile(i[0], i[1]):
                r = random.random()
                if r < 0.15:
                    kgbAgents.append(Ckgb(4,i[0],i[1]))

    elif difficulty == 'Hard':
        for i in range(0,20,1):
            for j in range(7,23,1):
                if (abs(5 - i) > 2 or abs(16 - j) > 2) and boardArray[i][j] != 1 and freeTile(i, j):
                    r = random.random()
                    if i >= 7 and i <= 17 and j >= 7 and j <= 14:
                        if r < 0.07:
                            kgbAgents.append(Ckgb(1,i,j))
                    elif i >= 0 and i <= 5 and j >= 9 and j <= 15:
                        if r < 0.18:
                            kgbAgents.append(Ckgb(1,i,j))
                    else:
                        if r < 0.1:
                            kgbAgents.append(Ckgb(1,i,j))

        for i in range(0,20,1):
            for j in range(7,23,1):
                if (abs(5 - i) > 2 or abs(16 - j) > 2) and freeTile(i, j):
                    r = random.random()
                    if boardArray[i][j] == 3:
                        if r < 0.08:
                            kgbAgents.append(Ckgb(2, i, j))
                    elif boardArray[i][j] == 4:
                        if r < 0.15:
                            kgbAgents.append(Ckgb(2, i, j))

        for i in range(0,20,1):
            for j in range(7,23,1):
                if (abs(5 - i) > 2 or abs(16 - j) > 2) and freeTile(i, j) and boardArray[i][j] != 1:
                    r = random.random()
                    if r < 0.06:
                        kgbAgents.append(Ckgb(3,i,j))

        for i in border:
            if freeTile(i[0], i[1]):
                r = random.random()
                if r < 0.2:
                    kgbAgents.append(Ckgb(4,i[0],i[1]))

    elif difficulty == 'Death':
        for i in range(0,20,1):
            for j in range(7,23,1):
                if (abs(5 - i) > 2 or abs(16 - j) > 2) and boardArray[i][j] != 1 and freeTile(i, j):
                    r = random.random()
                    if i >= 7 and i <= 17 and j >= 7 and j <= 14:
                        if r < 0.08:
                            kgbAgents.append(Ckgb(1,i,j))
                    elif i >= 0 and i <= 5 and j >= 9 and j <= 15:
                        if r < 0.2:
                            kgbAgents.append(Ckgb(1,i,j))
                    else:
                        if r < 0.11:
                            kgbAgents.append(Ckgb(1,i,j))

        for i in range(0,20,1):
            for j in range(7,23,1):
                if (abs(5 - i) > 2 or abs(16 - j) > 2) and freeTile(i, j):
                    r = random.random()
                    if boardArray[i][j] == 3:
                        if r < 0.1:
                            kgbAgents.append(Ckgb(2, i, j))
                    elif boardArray[i][j] == 4:
                        if r < 0.17:
                            kgbAgents.append(Ckgb(2, i, j))

        for i in range(0,20,1):
            for j in range(7,23,1):
                if (abs(5 - i) > 2 or abs(16 - j) > 2) and freeTile(i, j) and boardArray[i][j] != 1:
                    r = random.random()
                    if r < 0.08:
                        kgbAgents.append(Ckgb(3,i,j))

        for i in border:
            if freeTile(i[0], i[1]):
                r = random.random()
                if r < 0.25:
                    kgbAgents.append(Ckgb(4,i[0],i[1]))
                                         
            
        
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
##            if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
##                turn = turn + 1
##                mp = 6
##                for i in kgbAgents:
##                    if i.type == 4:
##                        r = random.random()
##                        if difficulty == 'Easy':
##                            if r < 0.25:
##                                i.move()
##                        elif difficulty == 'Medium':
##                            if r < 0.33:
##                                i.move()
##                        elif difficulty == 'Hard':
##                            if r < 0.37:
##                                i.move()
##                        elif difficulty == 'Death':
##                            if r < 0.45:
##                                i.move()
##                       
##                    elif i.type == 3:
##                        r = random.random()
##                        if r < 0.5:
##                            i.move()
##                    else:
##                        i.move()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_v and not evUsed:
                ev = True
                evUsed = True
                evTurn = turn
                pygame.mixer.Channel(4).play(saSound)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_o and not otrUsed:
                otr = True
                otrUsed = True
                otrTurn = turn
                pygame.mixer.Channel(5).play(saSound)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                if debug:
                    debug = False
                else:
                    debug = True

            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                pygame.quit()
                quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]

                if(player.getRow() == coordsToGrid(x,y)[0] and player.getColumn() == coordsToGrid(x,y)[1]):
                    keyHeld = True
                elif (x >= 953 and x <= 1197 and y >= 430 and y <= 463):
                    turn = turn + 1
                    mp = 6
                    pygame.mixer.Channel(1).play(nextTurnSound)
                    if ev:
                        if difficulty == 'Easy':
                            if turn - evTurn >= 4:
                                ev = False
                        else:
                            if turn - evTurn >= 3:
                                ev = False
                    if otr:
                        if difficulty == 'Easy':
                            if turn - otrTurn >= 4:
                                otr = False
                        else:
                            if turn - otrTurn >= 3:
                                otr = False
                        
                    
                    for i in kgbAgents:
                        if i.type == 4:
                            r = random.random()
                            if difficulty == 'Easy':
                                if r < 0.25:
                                    i.move()
                            elif difficulty == 'Medium':
                                if r < 0.33:
                                    i.move()
                            elif difficulty == 'Hard':
                                if r < 0.37:
                                    i.move()
                            elif difficulty == 'Death':
                                if r < 0.45:
                                    i.move()
                        elif i.type == 3:
                            r = random.random()
                            if r < 0.5:
                                i.move()
                        else:
                            i.move()
                elif (x >= 950 and x <= 992 and y >= 521 and y <= 563):
                    pygame.mixer.Channel(6).play(clickSound)
                    if toggleFreeTile:
                        toggleFreeTile = False
                    else:
                        toggleFreeTile = True
                        
                elif (x >= 1052 and x <= 1094 and y >= 521 and y <= 563):
                    pygame.mixer.Channel(6).play(clickSound)
                    if toggleCity:
                        toggleCity = False
                    else:
                        toggleCity = True
                elif (x >= 1156 and x <= 1198 and y >= 521 and y <= 563):
                    pygame.mixer.Channel(6).play(clickSound)
                    if toggleRail:
                        toggleRail = False
                    else:
                        toggleRail = True
                
                    
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if keyHeld:
                    keyHeld = False
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    grid = coordsToGrid(x, y)
                    if(player.getRow() != grid[0] or player.getColumn() != grid[1]):
                        if(abs(grid[0] - player.getRow()) <= 1 and abs(grid[1] - player.getColumn()) <= 1):
                            if((boardArray[player.getRow()][player.getColumn()] == 4 and boardArray[grid[0]][grid[1]] == 4) or (boardArray[player.getRow()][player.getColumn()] == 2 and boardArray[grid[0]][grid[1]] == 4) or (boardArray[player.getRow()][player.getColumn()] == 4 and boardArray[grid[0]][grid[1]] == 2)):
                                if(mp >= 2):
                                    player.row = grid[0]
                                    player.column = grid[1]
                                    mp = mp - 2
                            elif((boardArray[player.getRow()][player.getColumn()] == 6 and boardArray[grid[0]][grid[1]] == 6) or (boardArray[player.getRow()][player.getColumn()] == 2 and boardArray[grid[0]][grid[1]] == 6) or (boardArray[player.getRow()][player.getColumn()] == 6 and boardArray[grid[0]][grid[1]] == 2) or (boardArray[player.getRow()][player.getColumn()] == 6 and boardArray[grid[0]][grid[1]] == 4) or (boardArray[player.getRow()][player.getColumn()] == 4 and boardArray[grid[0]][grid[1]] == 6)):
                                if (mp >= 2):
                                    player.row = grid[0]
                                    player.column = grid[1]
                                    mp = mp - 2

                            elif((boardArray[player.getRow()][player.getColumn()] == 3 and boardArray[grid[0]][grid[1]] == 3) or (boardArray[player.getRow()][player.getColumn()] == 2 and boardArray[grid[0]][grid[1]] == 3) or (boardArray[player.getRow()][player.getColumn()] == 3 and boardArray[grid[0]][grid[1]] == 2) or (boardArray[player.getRow()][player.getColumn()] == 6 and boardArray[grid[0]][grid[1]] == 3) or (boardArray[player.getRow()][player.getColumn()] == 3 and boardArray[grid[0]][grid[1]] == 6)):
                                if(mp >= 3):
                                    player.row = grid[0]
                                    player.column = grid[1]
                                    mp = mp - 3
                            else:
                                if(mp >= 6):
                                    player.row = grid[0]
                                    player.column = grid[1]
                                    mp = mp - 6
        if difficulty == 'Easy':
            if turn %3 == 0 or turn == 1 or debug:
                visibility = 100
            elif ev:
                visibility = 2
            elif boardArray[player.getRow()][player.getColumn()] == 2:
                visibility = 2            
            else:
                visibility = 1
        elif difficulty == 'Medium' or difficulty == 'Hard':
            if turn %4 == 0 or turn == 1 or debug:
                visibility = 100
            elif ev:
                visibility = 2
            elif boardArray[player.getRow()][player.getColumn()] == 2:
                visibility = 2            
            else:
                visibility = 1
        if difficulty == 'Death':
            if turn %5 == 0 or turn == 1 or debug:
                visibility = 100
            elif ev:
                visibility = 2
            elif boardArray[player.getRow()][player.getColumn()] == 2:
                visibility = 2            
            else:
                visibility = 1
            
        if turn %4 == 0 or turn == 1 or debug:
            visibility = 100
        elif ev:
            visibility = 2
        elif boardArray[player.getRow()][player.getColumn()] == 2:
            visibility = 2            
        else:
            visibility = 1
            
        gameDisplay.fill(bgColor)
        place(mapg, 68, 52)
        place(rect, 43, 21)
        place(sidebar, 910, 21)
        message_display(difficulty, 1135, 71, 30, 'times new roman', black)
        message_display(str(mp), 1110, 121, 18, 'times new roman', black)
        if visibility == 100:
            message_display('All', 1065, 168, 18, 'times new roman', black)
        else:
            message_display(str(visibility) + ' tiles', 1065, 168, 18, 'times new roman', black)
            
        message_display("Press Q to Quit Game", 60, 710, 10, 'times new roman', black)
            
        if not evUsed:
            place(enhancedVision, 940, 251)
        if not otrUsed:
            place(offTheRadar, 940, 301)

        if ev:
            place(evActive, 940, 251)
        if otr:
            place(otrActive, 940, 301)
            
        if toggleFreeTile:
            for i in range(0,20,1):
                for j in range(0,24,1):
                    if boardArray[i][j] == 1:
                        coords = gridToCoords(i,j)
                        centralPlace(blueCircle, coords[0], coords[1], blueCircle.get_width(), blueCircle.get_height())

        if toggleCity:
            for i in range(0,20,1):
                for j in range(0,24,1):
                    if boardArray[i][j] == 2:
                        coords = gridToCoords(i,j)
                        centralPlace(whiteCircle, coords[0], coords[1], whiteCircle.get_width(), whiteCircle.get_height())

        if toggleRail:
            for i in range(0,20,1):
                for j in range(0,24,1):
                    if boardArray[i][j] == 3 or boardArray[i][j] == 4 or boardArray[i][j] == 6:
                        coords = gridToCoords(i,j)
                        centralPlace(yellowCircle, coords[0], coords[1], yellowCircle.get_width(), yellowCircle.get_height())
        if keyHeld:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    if (player.getRow() + i) >= 0 and (player.getRow() + i) <= 19 and (player.getColumn() + j) >= 0 and (player.getColumn() + j) <= 23 and not(i == 0 and j == 0):
                        grid = [player.getRow() + i, player.getColumn() + j]
                        coords = gridToCoords(player.getRow() + i, player.getColumn() + j)
                        if((boardArray[player.getRow()][player.getColumn()] == 4 and boardArray[grid[0]][grid[1]] == 4) or (boardArray[player.getRow()][player.getColumn()] == 2 and boardArray[grid[0]][grid[1]] == 4) or (boardArray[player.getRow()][player.getColumn()] == 4 and boardArray[grid[0]][grid[1]] == 2)):
                            if(mp >= 2):
                                centralPlace(greenCircle, coords[0], coords[1], greenCircle.get_width(), greenCircle.get_height())
                        elif((boardArray[player.getRow()][player.getColumn()] == 6 and boardArray[grid[0]][grid[1]] == 6) or (boardArray[player.getRow()][player.getColumn()] == 2 and boardArray[grid[0]][grid[1]] == 6) or (boardArray[player.getRow()][player.getColumn()] == 6 and boardArray[grid[0]][grid[1]] == 2) or (boardArray[player.getRow()][player.getColumn()] == 6 and boardArray[grid[0]][grid[1]] == 4) or (boardArray[player.getRow()][player.getColumn()] == 4 and boardArray[grid[0]][grid[1]] == 6)):
                            if mp >= 2:
                                centralPlace(greenCircle, coords[0], coords[1], greenCircle.get_width(), greenCircle.get_height())
                        elif((boardArray[player.getRow()][player.getColumn()] == 3 and boardArray[grid[0]][grid[1]] == 3) or (boardArray[player.getRow()][player.getColumn()] == 2 and boardArray[grid[0]][grid[1]] == 3) or (boardArray[player.getRow()][player.getColumn()] == 3 and boardArray[grid[0]][grid[1]] == 2) or (boardArray[player.getRow()][player.getColumn()] == 6 and boardArray[grid[0]][grid[1]] == 3) or (boardArray[player.getRow()][player.getColumn()] == 3 and boardArray[grid[0]][grid[1]] == 6)):
                            if(mp >= 3):
                                centralPlace(greenCircle, coords[0], coords[1], greenCircle.get_width(), greenCircle.get_height())
                        else:
                            if(mp >= 6):
                                centralPlace(greenCircle, coords[0], coords[1], greenCircle.get_width(), greenCircle.get_height())

            centralPlace(spy, x, y, spy.get_width(), spy.get_height())

        else:
            centralPlace(spy, gridToCoords(player.getRow(), player.getColumn())[0], gridToCoords(player.getRow(), player.getColumn())[1], spy.get_width(), spy.get_height())

        if visibility == 100:
            for i in kgbAgents:
                centralPlace(kgb, gridToCoords(i.getRow(), i.getColumn())[0], gridToCoords(i.getRow(), i.getColumn())[1], kgb.get_width(), kgb.get_height())
        else:
            for i in kgbAgents:
                if abs(player.getRow() - i.getRow()) <= visibility and abs(player.getColumn() - i.getColumn()) <= visibility:
                    centralPlace(kgb, gridToCoords(i.getRow(), i.getColumn())[0], gridToCoords(i.getRow(), i.getColumn())[1], kgb.get_width(), kgb.get_height())

        if not freeTile(player.getRow(), player.getColumn()) and not otr:
            finished = True
            won = False

        if boardArray[player.getRow(), player.getColumn()] == 1:
            finished = True
            won = True

        if not pygame.mixer.Channel(7).get_busy():
            pygame.mixer.Channel(7).play(musicArray[int(random.random()*len(musicArray))])
        pygame.display.update()
        clock.tick(60)

    if won:
        successLoop()
    else:
        deathLoop()


def successLoop():
    pygame.mixer.Channel(2).play(winSound)
    delay = 500
    startTime = pygame.time.get_ticks()
    start = False
    while not start:
        if pygame.time.get_ticks() - delay >= startTime:
            start = True
    
    place(successScreen, 0, 0)
    passed = True
    pygame.display.update()
    while passed:
        if not pygame.mixer.Channel(7).get_busy():
            pygame.mixer.Channel(7).play(musicArray[int(random.random()*len(musicArray))])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                passed = False
##                time.sleep(0.2)
                levelSelect()

def deathLoop():
    pygame.mixer.Channel(3).play(deathSound)
    delay = 500
    startTime = pygame.time.get_ticks()
    start = False
    while not start:
        if pygame.time.get_ticks() - delay >= startTime:
            start = True
    
    place(deathScreen, 0, 0)
    passed = True
    pygame.display.update()
    while passed:
        if not pygame.mixer.Channel(7).get_busy():
            pygame.mixer.Channel(7).play(musicArray[int(random.random()*len(musicArray))])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                passed = False
##                time.sleep(0.2)
                levelSelect()
    

titleLoop()
levelSelect()

##Things to do:
##    1. set grid numbers DONE
##    2. find sprites for spy and kgb DONE
##    3. methods to convert to and from grid/coords DONE
##    4. objects for spy and kgb DONE
##    5. movement DONE
##    6. kgb movement DONE
##    7. title/menu screen DONE
##    8. grid on/off, safe squares on/off DONE
##    9. Music/SFX
##    10. Balancing
