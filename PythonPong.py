import pygame
from Paddle import paddle
from Ball import ball
pygame.init()

class Pong(object):

    winWidht = 800
    winHeight = 700

    paddleSpeed = 20

    win = pygame.display.set_mode((winWidht, winHeight))
    pygame.display.set_caption('Pong')

    # Player
    GREEN = (0, 255, 0)
    paddleP = paddle(GREEN, 20, 60)
    paddleP.rect.x = 50
    paddleP.rect.y = winHeight / 2
    scoreP = 0

    # Enemy
    RED = (255, 0, 0)
    paddleE = paddle(RED, 20, 60)
    paddleE.rect.x = winWidht - 50
    paddleE.rect.y = winHeight / 2
    scoreE = 0

    # Enemy
    YELLOW = (255, 255, 0)
    paddleE1 = paddle(YELLOW, 60, 20)
    paddleE1.rect.x = winWidht / 2
    paddleE1.rect.y = 5
    scoreE1 = 0

    # Enemy
    BLUE = (0, 0, 255)
    paddleE2 = paddle(BLUE, 60, 20)
    paddleE2.rect.x = winWidht / 2
    paddleE2.rect.y = winHeight - 50
    scoreE2 = 0

    # Ball
    WHITE = (255, 255, 255)
    Ball = ball(WHITE, 10, 10, winWidht, winHeight)

    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(paddleP)
    all_sprites_list.add(paddleE)
    all_sprites_list.add(paddleE1)
    all_sprites_list.add(paddleE2)
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

         # Enemy inputs1
        if Ball.rect.x > paddleE1.rect.x:
            paddleE1.moveRight(paddleSpeed, winWidht)

        if Ball.rect.x < paddleE1.rect.x:
            paddleE1.moveLeft(paddleSpeed)

        # Enemy inputs2
        if Ball.rect.x > paddleE2.rect.x:
            paddleE2.moveRight(paddleSpeed, winWidht)

        if Ball.rect.x < paddleE2.rect.x:
            paddleE2.moveLeft(paddleSpeed)

        Ball.update()

        # Ball wallcheck
        if Ball.rect.x >= winWidht:
            scoreE -= 1
            Ball.rect.x = winWidht/2
            Ball.rect.y = winHeight/2
            Ball.velocity[0] = -Ball.velocity[0]
        if Ball.rect.x <= 0:
            scoreP -= 1
            Ball.rect.x = winWidht/2
            Ball.rect.y = winHeight/2
            Ball.velocity[0] = -Ball.velocity[0]
        if Ball.rect.y >= winHeight - 5:
            scoreE2 -= 1
            Ball.rect.x = winWidht/2
            Ball.rect.y = winHeight/2
            Ball.velocity[1] = -Ball.velocity[1]
        if Ball.rect.y <= 5:
            scoreE1 -= 1
            Ball.rect.x = winWidht/2
            Ball.rect.y = winHeight/2
            Ball.velocity[1] = -Ball.velocity[1]

        # Ball collide detect
        if pygame.sprite.collide_mask(Ball, paddleP) or pygame.sprite.collide_mask(Ball, paddleE) or pygame.sprite.collide_mask(Ball, paddleE1) or pygame.sprite.collide_mask(Ball, paddleE2):
            Ball.bounce()

        win.fill((0, 0, 0))

        all_sprites_list.draw(win)

        # Score update
        font = pygame.font.Font(None, 74)
        text = font.render(str(scoreP), 1, WHITE)
        win.blit(text, (10, winHeight / 2))
        text = font.render(str(scoreE), 1, WHITE)
        win.blit(text, (winWidht - 40, winHeight / 2))
        text = font.render(str(scoreE1), 1, WHITE)
        win.blit(text, (winWidht / 2, 10))
        text = font.render(str(scoreE2), 1, WHITE)
        win.blit(text, (winWidht / 2, winHeight - 70))

        pygame.display.update()

    pygame.quit()
