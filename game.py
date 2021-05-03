import pygame

from player import Player
from enemy import Enemy
from field import Field

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600



screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


isRunning = True

fail_sound = pygame.mixer.Sound('crash.wav')
music = pygame.mixer.music.load('music.wav')

pygame.mixer.music.play(-1)

player = Player(150, 390, 10, 10)
enemy = Enemy(250, 200, 5, 5, 15)
enemy2 = Enemy(250, 250, 5, 5, 15)
enemy3 = Enemy(500, 250, 5, 5, 15)
enemy4 = Enemy(500, 300, 5, 5, 15)

fieldImage = pygame.image.load('field.png')
fieldImage = pygame.transform.scale(fieldImage, (550,290))

fieldStart = Field(113,359,100,70)
fieldFinish = Field(540,160,100,70)

font = pygame.font.Font('freesansbold.ttf', 32)

def update():
    keys = pygame.key.get_pressed()
    player.move(keys)
    enemy.move(250,500)
    enemy2.move(250,500)
    enemy3.move(250,500)
    enemy4.move(250,500)
    
    if player.draw(screen).collidelist([enemy.draw(screen), enemy2.draw(screen), enemy3.draw(screen), enemy4.draw(screen)]) != -1:
        fail_sound.play()
        player.reset()
        player.deaths += 1
    if player.draw(screen).collidelist([fieldFinish.draw(screen)]) != -1:
        print("Finished")

def draw():
    screen.fill((183,175,250))
    screen.blit(fieldImage, (100,150))
    fieldStart.draw(screen)
    fieldFinish.draw(screen)
    player.draw(screen)
    enemy.draw(screen)
    enemy2.draw(screen)
    enemy3.draw(screen)
    enemy4.draw(screen)

    deathCounter = font.render("Deaths: " + str(player.deaths), True, (255,255,255))
    screen.blit(deathCounter, (300,50))
    
    pygame.display.update()

while isRunning:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
    
    update()
    
    draw()

    

pygame.quit()
