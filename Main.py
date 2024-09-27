import pygame, sys, random

from enemy import *
from player import *
from playerBullet import *
from enemyBullet import *

def Spawn():
    for x in range(50, 750, 150):
        for y in range(25,275,50):
            enemy = Enemy(x,y)
            enemies.append(enemy)
##            return

def getHighScore():
    file = open("highscores.txt", "r")
    num = file.readline()
    high = 0
    num.strip()
    while num != "":
        if int(num) > high:
            high =int(num)
        num = file.readline()
    return high

def playSong(song):
    pygame.mixer.init()
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()
    


pygame.init()

clock = pygame.time.Clock()
FPS = 60
size = width, height = 980, 640
black = 0,0,0
BG = pygame.image.load("anotheronebg.jpg")
BG = pygame.transform.scale(BG, size)
screen = pygame.display.set_mode(size)
white = 255,255,255
deepRed = 70,0,0

titleSong = "fusionTitleMusic.mp3"
pygame.mixer.init()
pygame.mixer.music.load(titleSong)
pygame.mixer.music.play()

healthIco = pygame.image.load("healthIcon.png").convert_alpha()
selectBullet = pygame.image.load("selectBullet.png").convert_alpha()
selectBullet = pygame.transform.scale(selectBullet, [48,48])
font = pygame.font.SysFont("impact", 30)

bulletSpeed = [0,8]

score = 0
highScoreText = "HIGHSCORE: "
highScore = getHighScore()


gameScreen = 0
title = font.render(" METROID INVADERS ", False, white)
startLabel = font.render("S T A R T", False, white)
exitLabel = font.render(" E X I T", False, white)
startRect = startLabel.get_rect()
exitRect = exitLabel.get_rect()
titleRect = title.get_rect()
startRect.center = (width //2, height //2 - 20)
exitRect.center = (width // 2, height//2 + 50)
titleRect.center = (width //2 , height //2 - 200)

selectRect = selectBullet.get_rect()
selectRect.midright = startRect.midleft



scoreText = "SCORE: "
score = 0



enemies = []
pBullets = []
eBullets = []

player = Player(width, height)


 
Spawn()

while True:
    #playSong(titleSong)
    if gameScreen == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if selectRect.midright == startRect.midleft:
                        selectRect.midright = exitRect.midleft
                    else:
                        selectRect.midright = startRect.midleft
                        
                if event.key == pygame.K_UP:
                    if selectRect.midright == exitRect.midleft:
                        selectRect.midright = startRect.midleft
                    else:
                        selectRect.midright = exitRect.midleft
                        
                if event.key == pygame.K_RETURN and selectRect.midright == startRect.midleft:
                    enemies = []
                    pBullets = []
                    eBullets = []
                    score = 0
                    player.health = 5
                    Spawn()
                    gameScreen = 1
                if event.key == pygame.K_RETURN and selectRect.midright == exitRect.midleft:
                    pygame.quit()
                    sys.exit()
        highScore = getHighScore()            
        highScoreLabel = font.render(highScoreText + str(highScore), False, white)
        highScoreLabelRect = highScoreLabel.get_rect()
        highScoreLabelRect.center = (width // 2, height - 100)
       
        screen.fill(deepRed)
        screen.blit(highScoreLabel, highScoreLabelRect)
        screen.blit(title, titleRect)
        screen.blit(selectBullet, selectRect)
        screen.blit(startLabel, startRect)
        screen.blit(exitLabel, exitRect)
        pygame.display.flip()
       
        
    if gameScreen == 1:
        #Exit Stuff
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.stop()
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = PlayerBullet(bulletSpeed, player.rect.center)
                    pBullets.append(bullet)


        #Enemy Stuff
        index = 0
        if len(enemies) <= 5:
            enemies[0].lastEnemy = True
        for enemy in enemies:
            enemy.fireRate = len(enemies) * 20
            if index == len(enemies) - 1 or enemy.rect.x != enemies[index+1].rect.x:
                if enemy.willFire():
                    if len(enemies) <= 5:
                        
                        tempSpeed = enemy.directionCalculate(player)
                        eBullet = EnemyBullet(tempSpeed, enemy.rect.center)
                        eBullet.lastEnemy = True
                        eBullets.append(eBullet)
                    else:
                        eBullet = EnemyBullet(bulletSpeed, enemy.rect.center)
                        eBullets.append(eBullet)
            index +=1
        
        #this makes enemies shift down
        for enemy in enemies:
            outOfBounds = enemy.outOfBounds(width)
            if outOfBounds:
                break

        if outOfBounds:
            for enemy in enemies:
                    enemy.shiftDown()
        #If an enemy collides with a player, you lose a life.      
        if enemy.collision(player):
             player.health -=1
             enemies.remove(enemy)
##        if player.health <= 0:
##            file = open("highscores.txt", "a")
##            file.write(str(score) + "\n")
##            file.close()
##            pygame.quit()
##            sys.exit()
##            gameScreen = 0
           
                
            
        #Draw Screen
    ##    screen.fill(deepRed)
        screen.blit(BG, [0,0])


        #Draw Enemy Bullets
        for bullet in eBullets:
            screen = bullet.draw(screen)
        remove = False
        for bullet in eBullets:
            bullet.update(FPS, player, bulletSpeed)
            if bullet.collision(player):
                player.health -=1
                if player.health <= 0:
                    file = open("highscores.txt", "a")
                    file.write(str(score) + "\n")
                    file.close()
##                    pygame.quit()
##                    sys.exit()
                    gameScreen = 0
                remove = True
            if bullet.delete(height) or remove:
                remove = False
                eBullets.remove(bullet)

        #Update Enemies  
        for enemy in enemies:
            enemy.update(FPS)
            screen = enemy.draw(screen)
            
        #Player Stuff
        player.update(FPS, width)
        player.draw(screen)



        #Player Bullet Stuff
        remove = False
        for bullet in pBullets:
            bullet.update(FPS)
            for enemy in enemies:
                if bullet.collision(enemy):
                    enemies.remove(enemy)
                    score += enemy.pointValue
                    remove = True
                    
            if bullet.delete()or remove:
                pBullets.remove(bullet)
                remove = False
                
        for bullet in pBullets:
            screen = bullet.draw(screen)
        #Draw Health 
        for x in range(60, 60 + 60 * player.health, 60):
            screen.blit(healthIco, (width - x, 10))

        #create and draw score
        scoreLabel = font.render(scoreText + str(score), False, white)
        screen.blit(scoreLabel, [10,10])

        highScoreLabel = font.render(highScoreText + str(highScore), False, white)
        screen.blit(highScoreLabel, [10,40])
        
        #respawn
        if len(enemies) == 0:
            Spawn()
       #End Stuff     
        pygame.display.flip()
        clock.tick(FPS)
            

