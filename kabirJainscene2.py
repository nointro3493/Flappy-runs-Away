import pygame
import time
pygame.init()
screen = pygame.display.set_mode([600,500])
bg_Field = pygame.image.load("field-backgroundresized.png")
imageOne = open("bluebird-midflap.png")
flappy = pygame.image.load
gloppy = pygame.image.load("redbird-midflap.png")
Bfly = pygame.image.load("butterfly.png")
Bfly = pygame.transform.flip(Bfly, True, False)
circleColor = (0, 0, 0)
BflyX = -50
BflyY = 150
circleX = 300
circleY = 260
bg_FieldX = 0
bg_FieldY = 0
flappyX = 450
flappyY = 250
gloppyX = 100
gloppyY = 250

myFont = pygame.font.SysFont("Arial",20)
text = myFont.render("Uh-oh flappy is flying away after that butterfly!", 2,(255, 0, 0))
while True:
    flag = 0
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
    screen.blit(bg_Field, (bg_FieldX, bg_FieldY))
    screen.blit(flappy, (flappyX, flappyY))
    screen.blit(gloppy, (gloppyX, gloppyY))
    screen.blit(Bfly, (BflyX, BflyY))
    screen.blit(text,(0,0))

    if BflyX < 650 and BflyY == 150:
        BflyX = BflyX + 5

    if BflyX > 450:
        flappy = pygame.transform.flip(flappy, True, False)


    pygame.display.flip()
    time.sleep(.15)
pygame.display.quit()
quit()