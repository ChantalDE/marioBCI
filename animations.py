import pygame
import random

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super(Coin, self).__init__()

        # add all sprites
        self.images = []
        self.images.append(pygame.image.load('images/coin/frame_00_delay-0.08s.png'))
        self.images.append(pygame.image.load('images/coin/frame_01_delay-0.08s.png'))
        self.images.append(pygame.image.load('images/coin/frame_02_delay-0.08s.png'))
        self.images.append(pygame.image.load('images/coin/frame_03_delay-0.08s.png'))
        self.images.append(pygame.image.load('images/coin/frame_04_delay-0.08s.png'))
        self.images.append(pygame.image.load('images/coin/frame_05_delay-0.08s.png'))
        self.images.append(pygame.image.load('images/coin/frame_06_delay-0.08s.png'))
        self.images.append(pygame.image.load('images/coin/frame_07_delay-0.08s.png'))
        self.images.append(pygame.image.load('images/coin/frame_08_delay-0.08s.png'))
        self.images.append(pygame.image.load('images/coin/frame_09_delay-0.08s.png'))

        self.index = 0  # start image
        self.image = self.images[self.index]

        self.x = 300
        self.y = 300

        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.radius = int(self.rect.width / 4)
        self.image = pygame.transform.scale(self.image, (100, 100))

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0

        self.image = self.images[self.index]
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.radius = int(self.rect.width / 4)

        # pygame.draw.circle(self.image, (0, 0, 255), (self.x, self.y), self.radius)

    def setCoinLocation(self, x, y):
        self.x = x
        self.y = y

    def moveCoin(self, screen):
        reward_x = random.randint(0, screen[0])
        reward_y = random.randint(0, screen[1])
        self.setCoinLocation(reward_x, reward_y)


class MarioSprite(pygame.sprite.Sprite):

    def __init__(self):
        super(MarioSprite, self).__init__()
        # add all sprites
        self.images = []
        self.images.append(pygame.image.load('images/mario1.gif'))
        self.images.append(pygame.image.load('images/mario2.gif'))
        self.index = 0  # start image
        self.image = self.images[self.index]
        self.x = 0
        self.y = 0
        # self.rect = pygame.Rect(self.x, self.y, 5, 5) #(posX, posY, sizeX, sizeY)
        self.image_right = self.images
        self.images_left = [pygame.transform.flip(image, True, False) for image in self.images]
        self.score = 0

        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.radius = int(self.rect.width / 4)

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0

        self.image = self.images[self.index]
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.radius = int(self.rect.width / 4)

        # pygame.draw.circle(self.image, (0, 0, 255), self.rect.center, self.radius)

    # self.checkCollision(sprite2)

    def checkCollision(self, sprite2, screen):
        col = pygame.sprite.collide_circle(self, sprite2)
        # print(self.rect.center, self.radius, sprite2.rect.center, sprite2.radius)

        if col:
            print("collide")
            self.score += 1
            sprite2.moveCoin(screen)

    def move(self, command):
        if command == "left":
            self.x -= 5

        if command == "right":
            self.x += 5

        if command == "drop":
            self.y -= 5

        if command == "lift":
            self.y += 5
