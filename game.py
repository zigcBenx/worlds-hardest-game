import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600



screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


isRunning = True


x = 50
y = 50

vel = 5

while isRunning:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_DOWN]:
        y += vel
    if keys[pygame.K_UP]:
        y -= vel

    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,0,0), (x,y,10,10))

    
    pygame.display.update()


pygame.quit()
