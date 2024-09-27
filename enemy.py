import pygame, sys, random, math

from SpriteSheetToList import *

pygame.init()

class Enemy:
    def __init__(self,x,y):
        
        self.dir = 2
        self.image = pygame.image.load("metroid.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, [126, 53])
        self.imageList = SpriteSheetToList(self.image, 2)
        self.mask = pygame.mask.from_surface(self.imageList[0])
                                            
        self.rect = self.imageList[0].get_rect()
        self.rect.topleft = [x,y]
        self.count = 0
        self.frames = 0
        self.animationSpeed = 4
        self.pointValue = 100

    def draw(self, screen):
        screen.blit(self.imageList[self.count%len(self.imageList)], self.rect)
        return screen

    def update(self, FPS):
        self.frames += 1
        self.rect.x += self.dir
        if (self.frames%(FPS/self.animationSpeed)):
            self.count +=1

    def outOfBounds(self, width):
        if self.rect.right > width or self.rect.left < 0:
            return True
        else:
            return False

    def shiftDown(self):
        self.dir = self.dir * -1
        self.rect.y +=40
    

    def willFire(self):
        if random.randint(1,self.fireRate) == 1:
            return True
        else:
            return False
    
    def collision(self, target):
        offset = x, y = (target.rect.left - self.rect.left,
                         target.rect.top - self.rect.top)
        if self.mask.overlap(target.mask, offset) != None:
            return True
        else:
            return False

    def directionCalculate(self, player):
        dx, dy = player.rect.x - self.rect.x, player.rect.y - self.rect.y
        dist = math.sqrt(dx**2 + dy **2)
        dx, dy = dx / dist, dy / dist
        speed = [dx * 10, dy * 10]
        return speed
    
