import pygame

from player import Player
from enemy import Enemy
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600



screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


isRunning = True


player = Player(50, 50, 10, 10)
enemy = Enemy(50, 100, 5, 5, 15)
enemy2 = Enemy(50, 150, 5, 5, 15)
enemy3 = Enemy(250, 150, 5, 5, 15)
enemy4 = Enemy(250, 200, 5, 5, 15)

font = pygame.font.Font('freesansbold.ttf', 32)

def update():
    keys = pygame.key.get_pressed()
    player.move(keys)
    enemy.move(50,250)
    enemy2.move(50,250)
    enemy3.move(50,250)
    enemy4.move(50,250)
    
    if player.draw(screen).collidelist([enemy.draw(screen), enemy2.draw(screen), enemy3.draw(screen), enemy4.draw(screen)]) != -1:
        player.reset()
        player.deaths += 1

def draw():
    screen.fill((183,175,250))
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
