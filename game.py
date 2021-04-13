import pygame

from player import Player
from enemy import Enemy
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600



screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


isRunning = True


player = Player(50, 50, 10, 10)
enemy = Enemy(100, 100, 5, 5, 15, (255,255,0))

def update():
    keys = pygame.key.get_pressed()
    player.move(keys)
    enemy.move(50,250)

def draw():
    screen.fill((0,0,0))
    player.draw(screen)
    enemy.draw(screen)
    pygame.display.update()

while isRunning:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
    
    update()
    
    draw()

    

pygame.quit()
