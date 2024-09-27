import pygame

def SpriteSheetToList(sourceImage, numColumns):
    imageList = []
    sourceRect = sourceImage.get_rect()
    spriteWidth = sourceRect.width / numColumns
    spriteHeight = sourceRect.height

    for column in range(numColumns):
        subImage = sourceImage.subsurface(pygame.Rect((spriteWidth*column,0),
                                                      (spriteWidth,
                                                       spriteHeight)))
        imageList.append(subImage)
    return imageList


        
