import pygame
import random
pygame.init()

SIZE = WIDTH, HEIGHT = 1300, 600
SCREEN = pygame.display.set_mode(SIZE)

WHITE = 255, 255, 255
BLACK = 0, 0, 0
RED = 255, 0, 0
GREEN = 0, 255, 0

# inherit Sprite class of pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        # calling parent class constructor
        super(Player, self).__init__()
        self.width = 50
        self.height = 50
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH/2 - self.width/2
        self.rect.y = HEIGHT - self.height - 10
        self.SPEED = 6
        self.moveX = 0
        self.playerHealth = 200

    def update(self):
        keyPressed = pygame.key.get_pressed()
        if keyPressed[pygame.K_RIGHT]:
            self.moveX = self.SPEED
        elif keyPressed[pygame.K_LEFT]:
            self.moveX = -self.SPEED
        else:
            self.moveX = 0
        self.rect.x += self.moveX


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.width = 50
        self.height = 50
        self.image = pygame.Surface((self.width, self.height))
        self.color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH-self.width)
        self.rect.y = random.randint(-HEIGHT, 0)
        self.SPEED = random.random()
        self.moveY = random.randint(1, 3)

    def update(self, *args, **kwargs) -> None:
        self.rect.y += 1
        if self.rect.y > HEIGHT:
            self.rect.x = random.randint(0, WIDTH - self.width)
            self.rect.y = random.randint(-HEIGHT, 0)


class Bullet:
    def __init__(self, x, y):
        super(Bullet, self).__init__()
        self.width = 50
        self.height = 50
        self.image = pygame.Surface((self.width, self.height))
        self.color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.moveY = 4

    def update(self):
        self.rectY -= self.moveY

    def fireBullet(self):
        pass


sprite_group = pygame.sprite.Group()
player = Player()
sprite_group.add(player)

playerGroup = pygame.sprite.Group()
playerGroup.add(player)

enemyGroup = pygame.sprite.Group()


clock = pygame.time.Clock
FPS = 60


def showHealth():
    playerHealth = player.playerHealth
    pygame.draw.rect(SCREEN, WHITE, (10, 10, playerHealth, 30))
    font = pygame.font.Sysfont


num_enemy = 20
for i in range(num_enemy):
    sprite_group.add(Enemy)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.fireBullet()

    SCREEN.fill(BLACK)
    sprite_group.draw(SCREEN)
    sprite_group.update()
    pygame.display.flip()
    clock.tick(FPS)
