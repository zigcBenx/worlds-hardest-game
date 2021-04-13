import pygame

class Player:
    def __init__(self, x, y, width, height, vel=5, color=(255,0,0)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.color = color

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.vel
        if keys[pygame.K_RIGHT] and self.x < 800 - self.height:
            self.x += self.vel
        if keys[pygame.K_DOWN] and self.y < 600 - self.height:
            self.y += self.vel
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= self.vel

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
