from random import randint
import pygame
from Paddle import paddle
from Ball import ball
from Special import Special
pygame.init()

class Pong(object):

    winWidht = 800
    winHeight = 700

    paddleSpeed = 20

    win = pygame.display.set_mode((winWidht, winHeight))
    pygame.display.set_caption('Pong')

    # Player
    GREEN = (0, 255, 0)
    paddleP = paddle(GREEN, 20, 60, "Player")
    paddleP.rect.x = 50
    paddleP.rect.y = winHeight / 2
    scoreP = 0

    # Enemy
    RED = (255, 0, 0)
    paddleE = paddle(RED, 20, 60, "Enemy")
    paddleE.rect.x = winWidht - 50
    paddleE.rect.y = winHeight / 2
    scoreE = 0


    # Ball
    WHITE = (255, 255, 255)
    Ball = ball(WHITE, 10, 10, winWidht, winHeight)

    specialSize = 20
    playersHit = False
    newSpecial = None
    SpecialsList = []

    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(paddleP)
    all_sprites_list.add(paddleE)
    all_sprites_list.add(Ball)

    run = True
    while run:
        pygame.time.delay(16)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Players inputs
        keys = pygame.key.get_pressed()
        #if keys[pygame.K_DOWN]:
        if Ball.rect.y > paddleP.rect.y:
            paddleP.moveDown(paddleSpeed, winHeight)

        #if keys[pygame.K_UP]:
        if Ball.rect.y < paddleP.rect.y:
            paddleP.moveUp(paddleSpeed)

        # Enemy inputs
        if Ball.rect.y > paddleE.rect.y + paddleE.rect.width / 2:
            paddleE.moveDown(paddleSpeed, winHeight)

        if Ball.rect.y < paddleE.rect.y+ paddleE.rect.width / 2:
            paddleE.moveUp(paddleSpeed)

        Ball.update()

        # Ball wallcheck
        if Ball.rect.x >= winWidht:
            scoreP += 1
            Ball.resetBall()
            Ball.rect.x = winWidht/2
            Ball.rect.y = winHeight/2
            Ball.velocity[0] = -Ball.velocity[0]
        if Ball.rect.x <= 0:
            scoreE += 1
            Ball.resetBall()
            Ball.rect.x = winWidht/2
            Ball.rect.y = winHeight/2
            Ball.velocity[0] = -Ball.velocity[0]

        if Ball.rect.y <= 0:
            Ball.velocity[1] = -Ball.velocity[1]
        if Ball.rect.y >= winHeight:
            Ball.velocity[1] = -Ball.velocity[1]


        # Ball collide detect
        if pygame.sprite.collide_mask(Ball, paddleP):
            Ball.bounce(paddleP)
            #if randint(0,3) is 2:
            playersHit = True
            newSpecial = Special(WHITE, specialSize, specialSize, winWidht, winHeight)
            SpecialsList.append(newSpecial)
            all_sprites_list.add(newSpecial)
        
        if pygame.sprite.collide_mask(Ball, paddleE):
            Ball.bounce(paddleE)            
            #if randint(0,3) is 2:
            playersHit = False
            newSpecial = Special(WHITE, specialSize, specialSize, winWidht, winHeight)
            SpecialsList.append(newSpecial)
            all_sprites_list.add(newSpecial)

        if newSpecial != None:
            for specials in SpecialsList:
                if pygame.sprite.collide_mask(Ball, specials):   
                    specials.rect.x = 400000
                    SpecialsList.pop()
                    specials = None

                    Ball.velocity[0] *= 1.01
                    Ball.MoreBalls()

                    if(playersHit is True):
                        paddleP.managePaddle(500)
                    else:
                        paddleE.managePaddle(500)

           
        win.fill((0, 0, 0))

        all_sprites_list.draw(win)

        # Score update
        font = pygame.font.Font(None, 74)
        text = font.render(str(scoreP), 1, WHITE)
        win.blit(text, (10, winHeight / 2))
        text = font.render(str(scoreE), 1, WHITE)
        win.blit(text, (winWidht - 40, winHeight / 2))


        pygame.display.update()

    pygame.quit()
