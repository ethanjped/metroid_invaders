import pygame

def moveShip(shipRect, speed, width, height):
    keys = pygame.key.get_pressed()
   
    if keys[pygame.K_RIGHT]:
        shipRect.x = shipRect.x + speed
    if keys[pygame.K_LEFT]:
        shipRect.x = shipRect.x -speed
    if keys[pygame.K_UP]:
        shipRect.y = shipRect.y -speed
    if keys[pygame.K_DOWN]:
        shipRect.y = shipRect.y +speed
    if shipRect.left < 0:
        shipRect.left = 0
    if shipRect.right > width:
        shipRect.right = width
    if shipRect.top < 0:
        shipRect.top = 0
    if shipRect.bottom > height:
        shipRect.bottom = height
    return shipRect
