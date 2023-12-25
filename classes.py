import pygame

class Hands:
  def __init__(self, damage, speed, length):
    self.damage = damage
    self.speed = speed
    self.length = length

class User:
    def __init__(self, speed, health):
        self.speed = speed
        self.health = health
        self.sprite = pygame.image.load('Images/err.webp')
        self.rect = self.sprite.get_rect()
        self.rect.x = 207.5
        self.rect.y = 400
        self.acc = pygame.Vector2(0, 0)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        self.acc = pygame.Vector2(0, 0)

        if pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]:
            self.acc.x = -1
        if pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]:
            self.acc.x = 1
        if pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_w]:
            self.acc.y = -1
        if pressed_keys[pygame.K_DOWN] or pressed_keys[pygame.K_s]:
            self.acc.y = 1

        self.rect.x += self.acc.x * self.speed
        self.rect.y += self.acc.y * self.speed

    def draw(self, screen):
        screen.blit(self.sprite, self.rect)