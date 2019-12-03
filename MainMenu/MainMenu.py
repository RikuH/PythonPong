import pygame
from Button import button

pygame.init()

winWidht = 800
winHeight = 700

PongButtonColor = (0, 255, 255)
ExitButtonColor = (255, 0, 0)

win = pygame.display.set_mode((winWidht, winHeight))
pygame.display.set_caption('MainMenu')

#PongButton
SBx = winWidht / 2
SBy = winHeight / 3
SBtext = "Pong"
StartButton = button(PongButtonColor, 150, 60, SBx, SBy)

#ExitButton
SBx = winWidht / 2
SBy = winHeight / 2
EBtext = "Exit"
ExitButton = button(ExitButtonColor, 150, 60, SBx, SBy)

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(StartButton)
all_sprites_list.add(ExitButton)

run = True
while run:
    pygame.time.delay(40)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((30, 30, 30))
    all_sprites_list.draw(win)
    StartButton.drawText(StartButton, SBtext, win)
    ExitButton.drawText(ExitButton, EBtext, win)

    if StartButton.rect.collidepoint(pygame.mouse.get_pos()):
        print ("Start")

    pygame.display.update()

pygame.quit()