import pygame
from random import randint

BLACK = (0, 0, 0)

winWidth = 0
winHeight = 0

class ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height, windowWidth, WindowHeight):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.velocity = [randint(4,8), randint(-5, 5)]

        self.rect = self.image.get_rect()

        winHeight = WindowHeight
        winWidth = windowWidth

        self.rect.x = windowWidth / 2
        self.rect.y = WindowHeight / 2

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self, paddle):
        self.velocity[0] = -self.velocity[0]

        if self.rect.y < paddle.rect.y + paddle.rect.width:
            self.velocity[1] = randint(-8, 0)
        else:
            self.velocity[1] = randint(0, 8)

    def resetBall(self):
        self.velocity = [randint(10, 15), randint(-8, 8)]

    def MoreBalls(self):       
        pygame.draw.rect(self.image, (200,200,200), [0, 0, 10, 10])
        pygame.draw.rect(self.image, (200,200,200), [0, 0, 10, 10])
        pygame.draw.rect(self.image, (200,200,200), [0, 0, 10, 10])
    


