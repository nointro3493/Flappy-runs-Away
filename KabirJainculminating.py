# K. Jain - Assig #7b - Pygame animation".
# Input:      Do you want to run the program, do you want to rerun the program
# Processing: N/A
# Output:     Story about bird getting lost.

def main():
    import pygame
    import time
    import sys

    pygame.init()
    screen = pygame.display.set_mode([900, 800])

    # image Loadingq
    imageFour = open("field-backgroundresized.png")
    imageOne = open("bluebird-midflap.png")
    imageOneFlip = open("bluebird-midflap.png")
    imageOneFlipF = open("bluebird-midflapF.png")
    imageTwo = open("redbird-midflap.png")
    imageThree = open("butterfly.png")
    imageFive = open("houseBg9.png")
    imageSix = open("dadBirdResized.png")
    imageSeven = open("momBird.png")
    imageTwoFlip = open("redbird-midflap.png")
    imageEight = open("desertBg.png")
    imageNine = open("treeResized.png")
    imageTen = open("titleSlide.png")

    # Sound Loading
    soundOne = "happyMusic.wav"
    soundTwo = "flappingWings.wav"
    soundFour = "epicMusic.wav"
    soundFive = "FastSpeaking.wav"
    soundSix = "crashNoise.wav"
    soundSeven = "cryingBaby.wav"
    soundEight = "happyKids.wav"
    soundTen = "happyMusic.wav"
    soundTwelve = "nervousMusic.wav"
    soundThirteen = "AwwSound.wav"

    pygame.mixer.music.load(soundOne)
    pygame.mixer.music.play(0)

    # image defining
    bg_Field = pygame.image.load(imageFour)
    flappy = pygame.image.load(imageOne)
    flappy = pygame.transform.flip(flappy, True, False)
    johnnyBird = pygame.image.load(imageTwo)
    butterfly = pygame.image.load(imageThree)
    bg_House = pygame.image.load(imageFive)
    dadBird = pygame.image.load(imageSix)
    dadBird = pygame.transform.flip(dadBird, True, False)
    momBird = pygame.image.load(imageSeven)
    momBird = pygame.transform.flip(momBird, True, False)
    johnnyBirdFLip = pygame.image.load(imageTwoFlip)
    johnnyBirdFLip = pygame.transform.flip(johnnyBirdFLip, True, False)
    bgDesert = pygame.image.load(imageEight)
    flippedFlappy = pygame.image.load(imageOneFlip)
    tree = pygame.image.load(imageNine)
    flippedFlappyOne = pygame.image.load(imageOneFlipF)
    titleSlide = pygame.image.load(imageTen)
    circleColor = (0, 255, 0)
    sunColor = (255, 255, 0)
    flowerColor = (255, 255, 0)
    startColor = (220, 109, 157)

    # X and Y coordinates of sprites and backgrounds
    bg_HouseX = 0
    bg_HouseY = 0
    bg_FieldX = 0
    bg_FieldY = 0

    # First scene
    circleX = 300
    circleY = 330
    flappyX = 700
    flappyY = 250
    johnnyBirdX = 50
    johnnyBirdY = 250

    # These rectangles were used so that when something was to happen at a certain time, we would find the coordinates of the
    # rectangle
    rectX = 0
    rectY = 850
    rectX1 = 0
    rectY1 = 850

    # Butter Fly X and Y
    butterflyX = -50
    butterflyY = 250

    # House scene
    momBirdX = 100
    momBirdY = 400
    dadBirdX = 130
    dadBirdY = 400
    johnnyBirdFLipX = 950
    johnnyBirdFLipY = 450

    # scene 5
    momBirdX2 = -160
    momBirdY2 = 800
    dadBirdX2 = -190
    dadBirdY2 = 800
    johnnyBirdFLipX2 = -160
    johnnyBirdFLipY2 = 800

    bgDesertX = 0
    bgDesertY = 0
    treeX = 475
    treeY = 200

    flippedFlappyX = -50
    flippedFlappyY = 50

    # Sun and flower coordinates
    sunX = 550
    sunY = 50
    flowerX = 800
    flowerY = 450

    # Objects for last scene
    johnnyBirdFLipX3 = -190
    johnnyBirdFLipY3 = 40

    momBirdX3 = -160
    momBirdY3 = 0

    dadBirdX3 = -190
    dadBirdY3 = 0

    flippedFlappyOneX = 630
    flippedFlappyOneY = 598

    rectX2 = 0
    rectY2 = 900

    rectX3 = 100
    rectY3 = 100

    rectX4 = 100
    rectY4 = 100

    # Cloud
    Oval1X = 300
    Oval1Y = 90
    Oval2X = 290
    Oval2Y = 50
    Oval3X = 320
    Oval3Y = 50
    Oval4X = 280
    Oval4Y = 50
    Oval5X = 320
    Oval5Y = 75

    # Flags and font
    flag = "left"
    flagOne = "start"
    flag2 = "left"
    CloudFlag = "left"
    myFont = pygame.font.SysFont("Impact", 25)
    endFont = pygame.font.SysFont("Times New Roman", 40)
    text = myFont.render("Flappy and Johnny are playing with their ball", 2, (250, 250, 250))

    scene = 0

    while True:
        event = pygame.event.poll()

        if event.type == pygame.QUIT:
            time.sleep(0)
            sys.exit()

        if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_q):
            sys.exit()

        # Scene Start
        if scene == 0:
            time.sleep(0)

            screen.fill((255, 255, 0))
            text9 = endFont.render("WELCOME!!!", 2, (0, 0, 0))
            text10 = endFont.render("To Start this Animation please press \"enter\" key", 2, (0, 0, 0))
            screen.blit(text9, (300, 400))
            screen.blit(text10, (50, 450))
            screen.blit(titleSlide, (300, 500))

            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_RETURN):
                scene = 1

        # scene 1
        if scene == 1:
            time.sleep(0)
            background = screen.blit(bg_Field, (bg_FieldX, bg_FieldY))
            pygame.draw.circle(screen, (255, 255, 0), (800, 100), 50, 0)
            pygame.draw.line(screen, (255, 255, 0), (800, 230), (800, -2), 5)
            pygame.draw.line(screen, (255, 255, 0), (670, 150), (915, 50), 5)
            pygame.draw.line(screen, (255, 255, 0), (670, 150), (915, 50), 5)
            pygame.draw.line(screen, (255, 255, 0), (675, 40), (920, 175), 5)
            screen.blit(flappy, (flappyX, flappyY))
            screen.blit(johnnyBird, (johnnyBirdX, johnnyBirdY))
            circle = pygame.draw.circle(screen, circleColor, (circleX, circleY), 10, 0)
            pygame.draw.ellipse(screen, (255, 255, 255), (Oval1X, Oval1Y, 70, 70), 0)
            pygame.draw.ellipse(screen, (255, 255, 255), (Oval2X, Oval2Y, 90, 50), 0)
            pygame.draw.ellipse(screen, (255, 255, 255), (Oval3X, Oval3Y, 90, 40), 0)
            pygame.draw.ellipse(screen, (255, 255, 255), (Oval4X, Oval4Y, 70, 50), 0)
            pygame.draw.ellipse(screen, (255, 255, 255), (Oval5X, Oval5Y, 75, 70), 0)
            screen.blit(butterfly, (butterflyX, butterflyY))
            screen.blit(text, (0, 650))
            flappyFliped = open("bluebird-midflap.png")

            # Scene 1
            if Oval1X >= 125 - 10 and CloudFlag == "left" and scene == 1:
                Oval1X = Oval1X - 5
                Oval2X = Oval2X - 5
                Oval3X = Oval3X - 5
                Oval4X = Oval4X - 5
                Oval5X = Oval5X - 5

            if Oval1X == 125 and scene == 1:
                CloudFlag = "right"

            if Oval1X >= 100 and CloudFlag != "left":
                Oval1X = Oval1X + 5
                Oval2X = Oval2X + 5
                Oval3X = Oval3X + 5
                Oval4X = Oval4X + 5
                Oval5X = Oval5X + 5

            if Oval1X == 760 and scene == 1:
                CloudFlag = "left"

            if circleX >= 125 - 10 and flag == "left" and scene == 1:
                circleX = circleX - 5

            if circleX == 125 and scene == 1:
                flag = "right"

            if circleX <= 765 - 10 and flag != "left" and scene == 1:
                circleX = circleX + 5

            if circleX == 760 and scene == 1:
                flag = "left"

            if flagOne == "start":
                rectX = rectX + 5

            if butterflyX <= 900:
                butterflyX = butterflyX + 3
                butterflyY = butterflyY - 1

            if butterflyX > 780:
                imageOne.close()
                imageOneF = open("bluebird-midflap.png")
                flappy = pygame.image.load(imageOneF)
                flappyX = flappyX + 5
                flappyY = flappyY - 3
                text = myFont.render("Uh-oh flappy is flying away after that butterfly!", 2, (250, 250, 250))
                johnnyBird = pygame.transform.flip(johnnyBird, True, False)

            if butterflyX > 800:
                pygame.mixer.music.stop()
                pygame.mixer.music.load(soundTwo)
                pygame.mixer.music.play(0)

            if butterflyX >= 900 and scene == 1:
                scene = 3

        # Scene #3
        if scene == 3:
            screen.blit(bg_House, (bg_HouseX, bg_HouseY))
            screen.blit(momBird, (momBirdX, momBirdY))
            screen.blit(dadBird, (dadBirdX, dadBirdY))
            screen.blit(johnnyBirdFLip, (johnnyBirdFLipX, johnnyBirdFLipY))
            rectangle2 = (rectX1, rectY1, 100, 50)
            pygame.draw.rect(screen, circleColor, rectangle2, 3)
            text = myFont.render("Johnny tells the parents what happened and they look for flappy", 2, (250, 250, 250))
            screen.blit(text, (0, 650))

            if johnnyBirdFLipX > 750 and flag2 == "left":
                johnnyBirdFLipX = johnnyBirdFLipX - 5
                johnnyBirdFLipY = johnnyBirdFLipY - 2

            if johnnyBirdFLipX == 750:
                flag2 = "right"

            if rectX1 == 300:
                pygame.mixer.music.stop()
                pygame.mixer.music.load(soundFive)
                pygame.mixer.music.play(0)

            if rectX1 <= 900:
                rectX1 = rectX1 + 5

            if rectX1 >= 800 and flag2 == "right":
                imageTwoFlip.close()
                imageTwoF = open("redbird-midflap.png")
                johnnyBirdFLip = pygame.image.load(imageTwoF)
                dadBirdX = dadBirdX + 5
                dadBirdY = dadBirdY - 2
                momBirdX = momBirdX + 5
                momBirdY = momBirdY - 2
                johnnyBirdFLipX = johnnyBirdFLipX + 5

            if rectX1 == 805:
                pygame.mixer.music.stop()
                pygame.mixer.music.load(soundFour)
                pygame.mixer.music.play(0)

            if dadBirdX >= 900:
                scene = 4

            # scene 4
        if scene == 4:
            text4 = myFont.render("Flappy realizes that he is far away from home and is worried", 2, (0, 0, 0))
            screen.blit(bgDesert, (bgDesertX, bgDesertY))
            screen.blit(text4, (0, 650))
            screen.blit(tree, (treeX, treeY))
            screen.blit(flippedFlappy, (flippedFlappyX, flippedFlappyY))
            pygame.draw.circle(screen, (255, 255, 0), (800, 100), 50, 0)
            pygame.draw.line(screen, (255, 255, 0), (800, 230), (800, -2), 5)
            pygame.draw.line(screen, (255, 255, 0), (670, 150), (915, 50), 5)
            pygame.draw.line(screen, (255, 255, 0), (675, 40), (920, 175), 5)

            if flippedFlappyX < 580:
                flippedFlappyX = flippedFlappyX + 5

            if flippedFlappyY < 600:
                flippedFlappyY = flippedFlappyY - 1

            if flippedFlappyX >= 530:
                text4 = myFont.render("OH NO! In all the worry, flappy crashed", 2, (0, 0, 0))
                screen.blit(text4, (0, 680))

            if flippedFlappyY < 625:
                flippedFlappyY = flippedFlappyY + 5

            if flippedFlappyX == 580:
                imageOneFlip.close()
                imageOneF1 = open("bluebird-midflapF.png")
                flippedFlappy = pygame.image.load(imageOneF1)
                pygame.mixer.music.stop()
                pygame.mixer.music.load(soundSix)
                pygame.mixer.music.play(0)

            if flippedFlappyY == 598:
                pygame.mixer.music.stop()
                pygame.mixer.music.load(soundSeven)
                pygame.mixer.music.play(0)

            if flippedFlappyY >= 525 and flippedFlappyX >= 555:
                text4 = myFont.render("Flappy is so scared and hurt. OH NO!", 2, (0, 0, 0))
                screen.blit(text4, (0, 710))

            if flippedFlappyY == 598:
                time.sleep(4)
                scene = 5

        if scene == 5:
            time.sleep(0)
            screen.blit(bgDesert, (bgDesertX, bgDesertY))
            screen.blit(momBird, (momBirdX2, momBirdY2))
            screen.blit(dadBird, (dadBirdX2, dadBirdY2))
            screen.blit(johnnyBirdFLip, (johnnyBirdFLipX2, johnnyBirdFLipY))
            pygame.draw.line(screen, (0, 255, 0), (800, 490), (800, 850), 5)
            pygame.draw.ellipse(screen, (255, 255, 255), (775, 360, 40, 50), 0)
            pygame.draw.ellipse(screen, (255, 255, 255), (825, 430, 50, 40), 0)
            pygame.draw.ellipse(screen, (255, 255, 255), (725, 430, 50, 40), 0)
            pygame.draw.ellipse(screen, (255, 255, 255), (775, 480, 40, 50), 0)
            flower = pygame.draw.circle(screen, flowerColor, (flowerX, flowerY), 50, 0)
            middleFlower = pygame.draw.circle(screen, (165, 42, 42), (flowerX, flowerY), 20, 0)
            screen.blit(butterfly, (750, 450))
            text5 = myFont.render("What a stroke of Luck! This is the same butterfly Flappy had chased!", 2, (0, 0, 0))
            pygame.draw.circle(screen, (255, 255, 0), (800, 100), 50, 0)
            pygame.draw.line(screen, (255, 255, 0), (800, 230), (800, -2), 5)
            pygame.draw.line(screen, (255, 255, 0), (670, 150), (915, 50), 5)
            pygame.draw.line(screen, (255, 255, 0), (675, 40), (920, 175), 5)
            screen.blit(text5, (0, 650))

            if dadBirdX2 == -185:
                pygame.mixer.music.stop()

            if dadBirdX2 < 600:
                dadBirdX2 = dadBirdX2 + 5
                dadBirdY2 = dadBirdY2 - 5
                momBirdX2 = momBirdX2 + 5
                momBirdY2 = momBirdY2 - 5
                johnnyBirdFLipX2 = johnnyBirdFLipX2 + 5
                johnnyBirdFLipY2 = johnnyBirdFLipY2 - 5

            if dadBirdX2 > 300 > dadBirdY2:
                dadBirdY2 = dadBirdY2 + 5
                momBirdY2 = momBirdY2 + 5
                johnnyBirdFLipY2 = johnnyBirdFLipY2 + 5

            if dadBirdX2 == -180:
                pygame.mixer.music.stop()
                pygame.mixer.music.load(soundTwelve)
                pygame.mixer.music.play()

            if dadBirdX2 == 300:
                pygame.mixer.music.stop()
                pygame.mixer.music.load(soundEight)
                pygame.mixer.music.play()

            if dadBirdX2 >= 300:
                text6 = myFont.render("Hooray We found an important clue!", 2, (0, 0, 0))
                screen.blit(text6, (530, 280))

            if momBirdX2 == 630:
                scene = 6
                time.sleep(3)

        if scene == 6:
            time.sleep(0)
            screen.blit(bgDesert, (bgDesertX, bgDesertY))
            screen.blit(tree, (treeX + 100, treeY))
            screen.blit(flippedFlappyOne, (flippedFlappyOneX, flippedFlappyOneY))
            text7 = myFont.render("Soon before long, Flappy was found safe and sound!!!", 2, (0, 0, 0))
            screen.blit(text7, (0, 720))
            screen.blit(momBird, (momBirdX3, momBirdY3))
            screen.blit(dadBird, (dadBirdX3, dadBirdY3))
            screen.blit(johnnyBirdFLip, (johnnyBirdFLipX3, johnnyBirdFLipY3))
            pygame.draw.circle(screen, (255, 255, 0), (800, 100), 50, 0)
            pygame.draw.line(screen, (255, 255, 0), (800, 230), (800, -2), 5)
            pygame.draw.line(screen, (255, 255, 0), (670, 150), (915, 50), 5)
            pygame.draw.line(screen, (255, 255, 0), (675, 40), (920, 175), 5)
            text10 = myFont.render("Flappys parents tell him he should never leave without telling", 2, (0, 0, 0))
            screen.blit(text10, (0, 750))

            rectangle2 = (rectX1, rectY1, 100, 50)

            if dadBirdX3 < 350:
                dadBirdX3 = dadBirdX3 + 5
                momBirdX3 = momBirdX3 + 5
                johnnyBirdFLipX3 = johnnyBirdFLipX3 + 5

            if dadBirdX3 == -185:
                pygame.mixer.music.stop()
                pygame.mixer.music.load(soundOne)
                pygame.mixer.music.play()

            if dadBirdY3 < 580:
                dadBirdY3 = dadBirdY3 + 5
                momBirdY3 = momBirdY3 + 5
                johnnyBirdFLipY3 = johnnyBirdFLipY3 + 5

            if dadBirdY3 == 575:
                imageOneFlipF.close()
                imageOneFlip = open("bluebird-midflapff.png")
                flippedFlappyOne = pygame.image.load(imageOneFlip)

            if dadBirdY3 == 580:
                text8 = myFont.render("MOM DAD JOHNNY! You found me!", 2, (0, 0, 0))
                screen.blit(text8, (520, 560))

            if flippedFlappyOneX > 520 and dadBirdY3 == 580:
                flippedFlappyOneX = flippedFlappyOneX - 5

            if flippedFlappyOneX == 530:
                pygame.mixer.music.stop()
                pygame.mixer.music.load(soundThirteen)
                pygame.mixer.music.play()

            if flippedFlappyOneX == 530:
                time.sleep(2)
                scene = 7

        #   Scene End
        if scene == 7:
            pygame.mixer.music.stop()
            screen.fill((255, 255, 0))
            text9 = endFont.render("GOOD BYE!!!", 2, (0, 0, 0))
            text10 = endFont.render("Press \"Q\" to quit or \"r\" to rerun the program", 2, (0, 0, 0))
            screen.blit(text10, (150, 450))
            screen.blit(text9, (200, 400))

            if event.type == pygame.QUIT:
                time.sleep(0)
                sys.exit()

            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_r):
                scene = 8

        if scene == 8:
            main()

        pygame.display.flip()
        time.sleep(0.03)


if __name__ == '__main__':
    window = main()
