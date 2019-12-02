import pygame
from Paddle import paddle
from Ball import ball
pygame.init()

winWidht = 800
winHeight = 700

paddleSpeed = 20

win = pygame.display.set_mode((winWidht, winHeight))

# Player
GREEN = (0, 255, 0)
paddleP = paddle(GREEN, 20, 60)
paddleP.rect.x = 50
paddleP.rect.y = 50
scoreP = 0

# Enemy
RED = (255, 0, 0)
paddleE = paddle(RED, 20, 60)
paddleE.rect.x = winWidht - 50
paddleE.rect.y = 50
scoreE = 0

# Ball
WHITE = (255, 255, 255)
Ball = ball(WHITE, 10, 10, winWidht, winHeight)

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(paddleP)
all_sprites_list.add(paddleE)
all_sprites_list.add(Ball)

run = True
while run:
    pygame.time.delay(40)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Players inputs
    keys = pygame.key.get_pressed()
    # if keys[pygame.K_DOWN]:
    if Ball.rect.y > paddleP.rect.y:
        paddleP.moveDown(paddleSpeed, winHeight)

    # if keys[pygame.K_UP]:
    if Ball.rect.y < paddleP.rect.y:
        paddleP.moveUp(paddleSpeed)

    # Enemy inputs
    if Ball.rect.y > paddleE.rect.y:
        paddleE.moveDown(paddleSpeed, winHeight)

    if Ball.rect.y < paddleE.rect.y:
        paddleE.moveUp(paddleSpeed)

    Ball.update()

    # Ball wallcheck
    if Ball.rect.x >= winWidht:
        scoreP += 1
        Ball.rect.x = winWidht/2
        Ball.rect.y = winHeight/2
        Ball.velocity[0] = -Ball.velocity[0]
    if Ball.rect.x <= 0:
        scoreE += 1
        Ball.rect.x = winWidht/2
        Ball.rect.y = winHeight/2
        Ball.velocity[0] = -Ball.velocity[0]
    if Ball.rect.y >= winHeight - 5:
        Ball.velocity[1] = -Ball.velocity[1]
    if Ball.rect.y <= 5:
        Ball.velocity[1] = -Ball.velocity[1]

    # Ball collide detect
    if pygame.sprite.collide_mask(Ball, paddleP) or pygame.sprite.collide_mask(Ball, paddleE):
        Ball.bounce()

    win.fill((0, 0, 0))

    all_sprites_list.draw(win)

    # Score update
    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreP), 1, WHITE)
    win.blit(text, (250, 10))
    text = font.render(str(scoreE), 1, WHITE)
    win.blit(text, (420, 10))

    pygame.display.update()

pygame.quit()
