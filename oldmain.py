import pygame, sys
from SpriteSheetToList import *
from shipMove import *
pygame.init()

# Define Variables

size = width, height = 640, 480
screen = pygame.display.set_mode(size)
black = 0,0,0
deepRed = 100,0,0
spriteSheet = pygame.image.load("ship.png").convert_alpha()
spriteSheet = pygame.transform.scale(spriteSheet, [128,64])
spriteList = SpriteSheetToList(spriteSheet, 2)

spriteRect = spriteList[0].get_rect()
clock = pygame.time.Clock()
FPS = 60
count = 0
frames = 0
animationSpeed = 8
shipSpeed = 5

# Game Loop

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
# This is what makes the animation speed work
    frames +=1
    if (frames %(FPS / animationSpeed) == 0):
        count +=1
    screen.fill(deepRed)
    #print (spriteRect)
    spriteRect = moveShip(spriteRect, shipSpeed, width, height)
    screen.blit(spriteList[count%len(spriteList)], spriteRect)
    pygame.display.flip()
    clock.tick(FPS)
    
