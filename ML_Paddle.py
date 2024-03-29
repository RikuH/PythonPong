import pygame
BLACK = (0, 0, 0)

class ml_paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()

    def moveUp(self, pixels):
        if self.rect.y > 5:
            self.rect.y -= pixels

    def moveDown(self, pixels, windowHeight):
        if self.rect.y <= windowHeight - 60:
            self.rect.y += pixels

    def moveRight(self, pixels, windowWidth):
        if self.rect.x < windowWidth - 60:
            self.rect.x += pixels
            
    def moveLeft(self, pixels):
        if self.rect.x > 5:
            self.rect.x -= pixels   
