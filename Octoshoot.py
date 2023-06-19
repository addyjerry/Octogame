import pygame


pygame.init()


#display
screen = pygame.display.set_mode((900,700))
title =pygame.display.set_caption('OCTOSHOOT')

#ball
ballimg =pygame.image.load('ball.png')
ballX =99
ballY =300

def ball(x,y):
    screen.blit(ballimg,(x,y))



#bullet
bulletImg =pygame.image.load('bullet.png')
bulletX =99
bulletY =311
bulletX_change =0.9
bulletY_change =0.2
bullet_state ='ready'

def bullet(x,y):
    global bullet_state
    bullet_state ='fire'
    screen.blit(bulletImg,(x + 49,y +12))


#player
playerImg =pygame.image.load('soldier.png')
playerX=50
playerY=600
playerX_change =0
playerY_change =0

#player function
def player(x,y):
    screen.blit(playerImg,(x,y))


#bricks
bricklImg=pygame.image.load('brickr.png')
bricklX=200
bricklY = 190

brickrImg=pygame.image.load('brickl.png')
brickrX =200
brickrY = 410

def brickr(x,y):
    screen.blit(brickrImg,(x,y))

def brickl(x,y):
    screen.blit(bricklImg,(x,y))




#Octopus
OctopusImg =pygame.image.load('octopus.png')
OctopusX =650
OctopusY =200
OctopusX_change =0
OctopusY_change =0.1

#function of octopus
def octopus(x,y):
    screen.blit(OctopusImg,(x,y))

game = True
while game:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        if event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5
            if event.key ==pygame.K_RIGHT:
                playerX_change = 0.5
            if event.key ==pygame.K_UP:
                playerY_change = -0.5
            if event.key ==pygame.K_z:
                playerY_change = 0.5
            if event.key ==pygame.K_SPACE:
                if bullet_state is 'ready':
                    bulletX =playerX
                    bulletY = playerY
                    bullet (bulletX,bulletY)
            



        if event.type == pygame.KEYUP:
            playerX_change =0
            playerY_change =0
             

    #octopus movement
    if OctopusY >=400:
        OctopusY_change = -0.1        
    elif OctopusY <=100:
        OctopusY_change =0.1
     

    #bricks
    brickr(brickrX,brickrY)
    brickl(bricklX,bricklY)

     #player
    playerY += playerY_change
    playerX += playerX_change
    player(playerX,playerY)
    if playerY >=550:
        playerY=550
    if playerY <=10:
        playerY =10
    if playerX >=550:
        playerX =550
    if playerX <=10:
        playerX=10

 
    #bullet
    if bulletX >=650:
            bullet_state ='ready'
    if bullet_state is 'fire':
        bullet (bulletX,bulletY)
        bulletX += bulletX_change 


    #ball


    #octopus
    octopus(OctopusX,OctopusY)
    OctopusX_change += OctopusX
    OctopusY += OctopusY_change

    pygame.display.update()