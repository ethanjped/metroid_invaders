import pygame, sys

from SpriteSheetToList import *

pygame.init()

class Player:
    def __init__(self, width, height):

        self.speed = 6
        self.image = pygame.image.load("samusSprite.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, [256, 128])
        self.imageList = SpriteSheetToList(self.image, 2)
        self.mask = pygame.mask.from_surface(self.imageList[0])

        self.rect = self.imageList[0].get_rect()
        self.rect.bottom = height
        self.rect.x = width/2
        self.animationSpeed = 4
        self.count = 0
        self.frames = 0
        self.health = 5

    def draw(self, screen):
        screen.blit(self.imageList[self.count%len(self.imageList)], self.rect)
        return screen

    def update(self, FPS,width):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.x = self.rect.x + self.speed
        if keys[pygame.K_LEFT]:
            self.rect.x = self.rect.x -self.speed
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > width:
            self.rect.right = width

        self.frames += 1
        if (self.frames%(FPS/self.animationSpeed)):
            self.count +=1

    

    
