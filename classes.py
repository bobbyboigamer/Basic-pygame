import pygame

class Hands:
  def __init__(self, damage, speed, length):
    self.damage = damage
    self.speed = speed
    self.length = length

class User:
    def __init__(self, speed, health, size):
        self.speed = speed
        self.health = health
        self.size = size
        self.sprite = pygame.image.load('Images/err.webp')
        self.sprite = pygame.transform.scale(self.sprite, self.size)
        self.rect = self.sprite.get_rect()
        self.rect.centerx = 510 / 2
        self.rect.bottom = 500
        self.acc = pygame.Vector2(0, 0)

    def update(self):
        MAX_WIDTH, MAX_HEIGHT = 510, 512.5
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

        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > MAX_WIDTH - self.rect.width:
            self.rect.x = MAX_WIDTH - self.rect.width

        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > MAX_HEIGHT - self.rect.height:
            self.rect.y = MAX_HEIGHT - self.rect.height

    def draw(self, screen):
        screen.blit(self.sprite, self.rect)