########################
## Alien Invasion.py
## By Ysaac Kingsley
## 12/3/2024


######### CODE ###########


import pygame
from random import randint

# pygame setup
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((720, 850))
clock = pygame.time.Clock()
running = True

playerImg = pygame.image.load('res/spaceship.png').convert_alpha()
bulletImg = pygame.image.load('res/plasma_ball.png').convert_alpha()
alien1 = pygame.image.load('res/alien1.png').convert_alpha()
alien2 = pygame.image.load('res/alien2.png').convert_alpha()
alien3 = pygame.image.load('res/alien3.png').convert_alpha()

highscoreFile = open('files/highscore.data', 'r+')
highscore = highscoreFile.read()
highscoreFile.close()

bullets = []
enemies = []

scoreFont = pygame.font.SysFont('Arial', 62)
highscoreFont = pygame.font.SysFont('Arial', 32)


##########CLASSESS##########

class Player():
    def __init__(self):
        self.pos = [360, 690]
        self.img = pygame.Surface((505, 513))
        self.dir = 0 # -1 for left 1 for right 0 for stationary
        self.speed = 3
        self.lives = 3
        self.img.blit(playerImg, (0, 0))
        
    def move(self):
        if self.dir == -1:
            self.pos[0] -= self.speed
        elif self.dir == 1:
            self.pos[0] += self.speed

    def shoot(self):
        bullets.append(Bullet(self.pos[0], self.pos[1]))


class Bullet():
    def __init__(self, x, y):
        self.pos = [x, y]
        self.img = pygame.Surface((503, 545))
        self.speed = 3
        self.img.blit(bulletImg, (0, 0))

class Enemy():
    def __init__(self, x, y, endX, dir):
        self.pos = [x, y]
        self.endX = endX
        self.dir = dir


class BaseEnemy(Enemy):
    def __init__(self, x, y, endX, dir):
        super().__init__(x, y, endX, dir)
        self.img = pygame.Surface((747, 557))
        self.speed = 2
        self.health = 10
        self.img.blit(alien1, (0, 0))

class EnemyLevel2(Enemy):
    def __init__(self, x, y, endX, dir):
        super().__init__(x, y, endX, dir)
        self.img = pygame.Surface((280, 133))
        self.speed = 3
        self.health = 20
        self.img.blit(alien2, (0, 0))

class EnemyLevel3(Enemy):
    def __init__(self, x, y, endX, dir):
        super().__init__(x, y, endX, dir)
        self.img = pygame.Surface((320, 220))
        self.speed = 4
        self.health = 40
        self.img.blit(alien3, (0, 0))


player = Player()

score = 0
gameOver = False
spawnEmemiesCounter = 0 # when gets to spawnEnemiesMax call spawn enemies, decrement spawnEnemiesMax by 1
spawnEnemiesMax = 300
formationCounter = 0
formationCounterMax = 900
formationAmt = 2
respawnTimer = 0
respawnTimerMax = 180
respawned = True
offset = -200

seconds = 0
secondsCounter = 0
secondsMax = 60


########## FUNCTIONS ########


def move_bullets():
    for bullet in bullets:
        bullet.pos[1] -= bullet.speed
        if bullet.pos[1] <= -60:
            bullets.remove(bullet)

def move_enemies():
    for enemy in enemies:
        enemy.pos[1] += enemy.speed
        if enemy.pos[0] < enemy.endX and enemy.dir == 1:
            enemy.pos[0] += enemy.speed
        elif enemy.pos[0] > enemy.endX and enemy.dir == -1:
            enemy.pos[0] -= enemy.speed
        if enemy.pos[1] >= 850:
            enemies.remove(enemy)

def spawn_enemies(f):
    #formation = randint (0, 4)
    formation = f
    if formation == 0:
        et1 = randint(0, 2)
        et2 = randint(0, 2)
        et3 = randint(0, 2)
        et4 = randint(0, 2)
        et5 = randint(0, 2)
        et6 = randint(0, 2)
        et7 = randint(0, 2)
        et8 = randint(0, 2)
        if et1 == 0:
            enemies.append(BaseEnemy(-240, 130, 20, 1))
        elif et1 == 1:
            enemies.append(EnemyLevel2(-240, 130, 20, 1))
        elif et1 == 2:
            enemies.append(EnemyLevel3(-240, 130, 20, 1))
        if et2 == 0:
            enemies.append(BaseEnemy(-180, 200, 80, 1))
        elif et2 == 1:
            enemies.append(EnemyLevel2(-180, 200, 80, 1))
        elif et2 == 2:
            enemies.append(EnemyLevel3(-180, 200, 80, 1))
        if et3 == 0:
            enemies.append(BaseEnemy(-120, 270, 120, 1))
        elif et3 == 1:
            enemies.append(EnemyLevel2(-120, 270, 120, 1))
        elif et3 == 2:
            enemies.append(EnemyLevel3(-120, 270, 120, 1))
        if et4 == 0:
            enemies.append(BaseEnemy(-60, 340, 180, 1))
        elif et4 == 1:
            enemies.append(EnemyLevel2(-60, 340, 180, 1))
        elif et4 == 2:
            enemies.append(EnemyLevel3(-60, 340, 180, 1))
        if et5 == 0:
            enemies.append(BaseEnemy(720, 340, 460, -1))
        elif et5 == 1:
            enemies.append(EnemyLevel2(720, 340, 460, -1))
        elif et5 == 2:
            enemies.append(EnemyLevel3(720, 340, 460, -1))
        if et6 == 0:
            enemies.append(BaseEnemy(780, 270, 520, -1))
        elif et6 == 1:
            enemies.append(EnemyLevel2(780, 270, 520, -1))
        elif et6 == 2:
            enemies.append(EnemyLevel3(780, 270, 520, -1))
        if et7 == 0:
            enemies.append(BaseEnemy(840, 200, 580, -1))
        elif et7 == 1:
            enemies.append(EnemyLevel2(840, 200, 580, -1))
        elif et7 == 2:
            enemies.append(EnemyLevel3(840, 200, 580, -1))
        if et8 == 0:
            enemies.append(BaseEnemy(900, 130, 640, -1))
        elif et8 == 1:
            enemies.append(EnemyLevel2(900, 130, 640, -1))
        elif et8 == 2:
            enemies.append(EnemyLevel3(900, 130, 640, -1))
    
    elif formation == 1:
        et1 = randint(0, 2)
        et2 = randint(0, 2)
        et3 = randint(0, 2)
        et4 = randint(0, 2)
        et5 = randint(0, 2)
        et6 = randint(0, 2)
        et7 = randint(0, 2)
        et8 = randint(0, 2)
        if et1 == 0:
            enemies.append(BaseEnemy(-240, 40, 20, 1))
        elif et1 == 1:
            enemies.append(EnemyLevel2(-240, 40, 20, 1))
        elif et1 == 2:
            enemies.append(EnemyLevel3(-240, 40, 20, 1))
        if et2 == 0:
            enemies.append(BaseEnemy(-180, 110, 80, 1))
        elif et2 == 1:
            enemies.append(EnemyLevel2(-180, 110, 80, 1))
        elif et2 == 2:
            enemies.append(EnemyLevel3(-180, 110, 80, 1))
        if et3 == 0:
            enemies.append(BaseEnemy(-120, 180, 120, 1))
        elif et3 == 1:
            enemies.append(EnemyLevel2(-120, 180, 120, 1))
        elif et3 == 2:
            enemies.append(EnemyLevel3(-120, 180, 120, 1))
        if et4 == 0:
            enemies.append(BaseEnemy(-60, 250, 180, 1))
        elif et4 == 1:
            enemies.append(EnemyLevel2(-60, 250, 180, 1))
        elif et4 == 2:
            enemies.append(EnemyLevel3(-60, 250, 180, 1))
        if et5 == 0:
            enemies.append(BaseEnemy(720, 270, 460, -1))
        elif et5 == 1:
            enemies.append(EnemyLevel2(720, 270, 460, -1))
        elif et5 == 2:
            enemies.append(EnemyLevel3(720, 270, 460, -1))
        if et6 == 0:
            enemies.append(BaseEnemy(780, 200, 520, -1))
        elif et6 == 1:
            enemies.append(EnemyLevel2(780, 200, 520, -1))
        elif et6 == 2:
            enemies.append(EnemyLevel3(780, 200, 520, -1))
        if et7 == 0:
            enemies.append(BaseEnemy(840, 130, 580, -1))
        elif et7 == 1:
            enemies.append(EnemyLevel2(840, 130, 580, -1))
        elif et7 == 2:
            enemies.append(EnemyLevel3(840, 130, 580, -1))
        if et8 == 0:
            enemies.append(BaseEnemy(900, 60, 640, -1))
        elif et8 == 1:
            enemies.append(EnemyLevel2(900, 60, 640, -1))
        elif et8 == 2:
            enemies.append(EnemyLevel3(900, 60, 640, -1))
    
    elif formation == 2:
        et1 = randint(0, 2)
        et2 = randint(0, 2)
        et3 = randint(0, 2)
        et4 = randint(0, 2)
        et5 = randint(0, 2)
        et6 = randint(0, 2)
        et7 = randint(0, 2)
        et8 = randint(0, 2)
        if et1 == 0:
            enemies.append(BaseEnemy(-240, -10, 20, 1))
        elif et1 == 1:
            enemies.append(EnemyLevel2(-240, -10, 20, 1))
        elif et1 == 2:
            enemies.append(EnemyLevel3(-240, -10, 20, 1))
        if et2 == 0:
            enemies.append(BaseEnemy(-180, 60, 80, 1))
        elif et2 == 1:
            enemies.append(EnemyLevel2(-180, 60, 80, 1))
        elif et2 == 2:
            enemies.append(EnemyLevel3(-180, 60, 80, 1))
        if et3 == 0:
            enemies.append(BaseEnemy(-120, 130, 120, 1))
        elif et3 == 1:
            enemies.append(EnemyLevel2(-120, 130, 120, 1))
        elif et3 == 2:
            enemies.append(EnemyLevel3(-120, 130, 120, 1))
        if et4 == 0:
            enemies.append(BaseEnemy(-60, 200, 180, 1))
        elif et4 == 1:
            enemies.append(EnemyLevel2(-60, 200, 180, 1))
        elif et4 == 2:
            enemies.append(EnemyLevel3(-60, 200, 180, 1))
        if et5 == 0:
            enemies.append(BaseEnemy(720, 200, 460, -1))
        elif et5 == 1:
            enemies.append(EnemyLevel2(720, 200, 460, -1))
        elif et5 == 2:
            enemies.append(EnemyLevel3(720, 200, 460, -1))
        if et6 == 0:
            enemies.append(BaseEnemy(780, 130, 520, -1))
        elif et6 == 1:
            enemies.append(EnemyLevel2(780, 130, 520, -1))
        elif et6 == 2:
            enemies.append(EnemyLevel3(780, 130, 520, -1))
        if et7 == 0:
            enemies.append(BaseEnemy(840, 60, 580, -1))
        elif et7 == 1:
            enemies.append(EnemyLevel2(840, 60, 580, -1))
        elif et7 == 2:
            enemies.append(EnemyLevel3(840, 60, 580, -1))
        if et8 == 0:
            enemies.append(BaseEnemy(900, -10, 640, -1))
        elif et8 == 1:
            enemies.append(EnemyLevel2(900, -10, 640, -1))
        elif et8 == 2:
            enemies.append(EnemyLevel3(900, 60, 640, -1))

    elif formation == 3:
        et1 = randint(0, 2)
        et2 = randint(0, 2)
        et3 = randint(0, 2)
        et4 = randint(0, 2)
        et5 = randint(0, 2)
        et6 = randint(0, 2)
        et7 = randint(0, 2)
        et8 = randint(0, 2)
        if et1 == 0:
            enemies.append(BaseEnemy(60, -60, 60, 0))
        elif et1 == 1:
            enemies.append(EnemyLevel2(60, -60, 60, 0))
        elif et1 == 2:
            enemies.append(EnemyLevel3(60, -60, 60, 0))
        if et2 == 0:
            enemies.append(BaseEnemy(120, -60, 120, 0))
        elif et2 == 1:
            enemies.append(EnemyLevel2(120, -60, 120, 0))
        elif et2 == 2:
            enemies.append(EnemyLevel3(120, -60, 120, 0))
        if et3 == 0:
            enemies.append(BaseEnemy(180, -60, 180, 0))
        elif et3 == 1:
            enemies.append(EnemyLevel2(180, -60, 180, 0))
        elif et3 == 2:
            enemies.append(EnemyLevel3(180, -60, 180, 0))
        if et4 == 0:
            enemies.append(BaseEnemy(240, -60, 240, 0))
        elif et4 == 1:
            enemies.append(EnemyLevel2(240, -60, 240, 0))
        elif et4 == 2:
            enemies.append(EnemyLevel3(240, -60, 240, 0))
        if et5 == 0:
            enemies.append(BaseEnemy(300, -60, 300, 0))
        elif et5 == 1:
            enemies.append(EnemyLevel2(300, -60, 300, 0))
        elif et5 == 2:
            enemies.append(EnemyLevel3(300, -60, 300, 0))
        if et6 == 0:
            enemies.append(BaseEnemy(360, -60, 360, 0))
        elif et6 == 1:
            enemies.append(EnemyLevel2(360, -60, 360, 0))
        elif et6 == 2:
            enemies.append(EnemyLevel3(360, -60, 360, 0))
        if et7 == 0:
            enemies.append(BaseEnemy(420, -60, 420, 0))
        elif et7 == 1:
            enemies.append(EnemyLevel2(420, -60, 420, 0))
        elif et7 == 2:
            enemies.append(EnemyLevel3(420, -60, 420, 0))
        if et8 == 0:
            enemies.append(BaseEnemy(480, -60, 480, 0))
        elif et8 == 1:
            enemies.append(EnemyLevel2(480, -60, 480, 0))
        elif et8 == 2:
            enemies.append(EnemyLevel3(480, -60, 480, 0))

    elif formation == 4:
        et1 = randint(0, 2)
        et2 = randint(0, 2)
        et3 = randint(0, 2)
        et4 = randint(0, 2)
        et5 = randint(0, 2)
        et6 = randint(0, 2)
        et7 = randint(0, 2)
        et8 = randint(0, 2)
        if et1 == 0:
            enemies.append(BaseEnemy(60, -120, 60, 0))
        elif et1 == 1:
            enemies.append(EnemyLevel2(60, -120, 60, 0))
        elif et1 == 2:
            enemies.append(EnemyLevel3(60, -120, 60, 0))
        if et2 == 0:
            enemies.append(BaseEnemy(120, -120, 120, 0))
        elif et2 == 1:
            enemies.append(EnemyLevel2(120, -120, 120, 0))
        elif et2 == 2:
            enemies.append(EnemyLevel3(120, -120, 120, 0))
        if et3 == 0:
            enemies.append(BaseEnemy(180, -120, 180, 0))
        elif et3 == 1:
            enemies.append(EnemyLevel2(180, -120, 180, 0))
        elif et3 == 2:
            enemies.append(EnemyLevel3(180, -120, 180, 0))
        if et4 == 0:
            enemies.append(BaseEnemy(240, -120, 240, 0))
        elif et4 == 1:
            enemies.append(EnemyLevel2(240, -120, 240, 0))
        elif et4 == 2:
            enemies.append(EnemyLevel3(240, -120, 240, 0))
        if et5 == 0:
            enemies.append(BaseEnemy(300, -120, 300, 0))
        elif et5 == 1:
            enemies.append(EnemyLevel2(300, -120, 300, 0))
        elif et5 == 2:
            enemies.append(EnemyLevel3(300, -120, 300, 0))
        if et6 == 0:
            enemies.append(BaseEnemy(360, -120, 360, 0))
        elif et6 == 1:
            enemies.append(EnemyLevel2(360, -120, 360, 0))
        elif et6 == 2:
            enemies.append(EnemyLevel3(360, -120, 360, 0))
        if et7 == 0:
            enemies.append(BaseEnemy(420, -120, 420, 0))
        elif et7 == 1:
            enemies.append(EnemyLevel2(420, -120, 420, 0))
        elif et7 == 2:
            enemies.append(EnemyLevel3(420, -120, 420, 0))
        if et8 == 0:
            enemies.append(BaseEnemy(480, -120, 480, 0))
        elif et8 == 1:
            enemies.append(EnemyLevel2(480, -120, 480, 0))
        elif et8 == 2:
            enemies.append(EnemyLevel3(480, -120, 480, 0))



def collision_detection():
    global score
    global gameOver
    global offset
    global highscore
    global respawned
    for i in range(len(bullets)):
        bulletRect = pygame.Rect(bullets[i].pos[0], bullets[i].pos[1], 60, 60)
        didCollide = False
        for e in range(len(enemies)):
            enemyRect = pygame.Rect(enemies[e].pos[0], enemies[e].pos[1]+offset, 60, 60)
            if (bulletRect.colliderect(enemyRect)):
                bullets.pop(i)
                didCollide = True
                enemies[e].health -= 10
                score+=10
                if (enemies[e].health <= 0):
                    enemies.pop(e)
                    score+=20
                break
        if didCollide:
            break
    if respawned:
        playerRect = pygame.Rect(player.pos[0], player.pos[1], 60, 60)
        for enemy in enemies:
            enemyRect = pygame.Rect(enemy.pos[0], enemy.pos[1]+offset, 60, 60)
            if playerRect.colliderect(enemyRect):
                respawned = False
                player.lives -= 1
                if (player.lives > -1):
                    player.pos[0] = 360
                else:
                    gameOver = True
                    highscore = highscore.split(' ')
                    highscore = int(highscore[1])
                    if (score > highscore):
                        highscore = score
                        highscoreFile = open('files/highscore.data', 'w')
                        highscoreFile.write('Highscore: ' + str(highscore))
                        highscore = 'Highscore: ' + str(highscore)
                        highscoreFile.close() 
                    
                

########## MAIN LOOP ##########


while running:
    if secondsCounter == secondsMax:
        secondsCounter = 0
        seconds += 1
    else:
        secondsCounter += 1
    print(seconds)
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if not gameOver:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.dir = -1
                elif event.key == pygame.K_d:
                    player.dir = 1
                if event.key == pygame.K_SPACE:
                    player.shoot()
                elif event.key == pygame.K_1:
                    spawn_enemies(0)
                elif event.key == pygame.K_2:
                    spawn_enemies(1)
                elif event.key == pygame.K_3:
                    spawn_enemies(2)
                elif event.key == pygame.K_4:
                    spawn_enemies(3)
                elif event.key == pygame.K_5:
                    spawn_enemies(4)
            elif event.type == pygame.KEYUP:
                player.dir = 0

    screen.fill('black')
    if not gameOver:
        player.move()
        move_bullets()
        move_enemies()
        collision_detection()

        if spawnEmemiesCounter >= spawnEnemiesMax:
            spawnAmount = randint(1, formationAmt)
            for i in range(spawnAmount):
                formation = randint(0, 4)
                spawn_enemies(formation)
            if spawnEnemiesMax >= 10:
                spawnEnemiesMax -= 1
            spawnEmemiesCounter = 0
        else:
            spawnEmemiesCounter+=1

        if formationCounter >= formationCounterMax:
            formationCounter = 0
            formationAmt += 1
        else:
            formationCounter += 1

        if respawnTimer >= respawnTimerMax:
            respawnTimer = 0
            respawned = True
        elif respawned == False:
            respawnTimer += 1


    screen.blit(pygame.transform.scale(player.img, (60, 60)), pygame.Rect(player.pos[0], player.pos[1], 60, 60))

    for enemy in enemies:
        screen.blit(pygame.transform.scale(enemy.img, (60, 60)), pygame.Rect(enemy.pos[0], enemy.pos[1]+offset, 60, 60))

    for bullet in bullets:
        screen.blit(pygame.transform.scale(bullet.img, (60, 60)), pygame.Rect(bullet.pos[0], bullet.pos[1], 60, 60))

    scoreSurface = scoreFont.render(str(score), False, (255, 255, 255))
    screen.blit(scoreSurface, (350, 10))

    highscoreSurface = highscoreFont.render(highscore, False, (255, 255, 255))
    screen.blit(highscoreSurface, (480, 10))

    livesSurface = scoreFont.render(f'x{player.lives}', False, (255, 255, 255))
    screen.blit(pygame.transform.scale(player.img, (40, 40)), (10, 20))
    screen.blit(livesSurface, (50, 20))

    if gameOver:
        gameOverSurface = scoreFont.render('Game Over!', False, (255, 255, 255))
        screen.blit(gameOverSurface, (200, 300))


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()