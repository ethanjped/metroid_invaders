import pygame, sys

from SpriteSheetToList import*

pygame.init()

class EnemyBullet:
    def __init__(self, speed, position):
        self.image = pygame.image.load("redBeam.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, [192,96])
        self.imageList = SpriteSheetToList(self.image, 2)
        self.mask = pygame.mask.from_surface(self.imageList[0])
        self.speed = speed
        self.rect = self.imageList[0].get_rect()
        self.rect.center = position
        self.animationSpeed = 4
        self.count = 0
        self.frames = 0
        self.lastEnemy = 0

    
    def draw(self, screen):
        screen.blit(self.imageList[self.count%len(self.imageList)], self.rect)
        return screen

    def update(self,FPS, player, speed):
        if self.lastEnemy:
##            print("dude!")
            self.rect.x += self.speed[0]
            self.rect.y += self.speed[1]
        else:
            self.rect.y += self.speed[1]
            
        #self.rect.y += self.speed[1]
        self.frames +=1
        if(self.frames%(FPS/self.animationSpeed)):
            self.count +=1

    def delete(self, height):
        if self.rect.y > height:
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
        
        
