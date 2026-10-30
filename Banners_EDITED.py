"""
Author: Moises Santander
Course: ETE 4990 FA2026
Purpose: Calls classes for other banners: StartScreen, EndScreen, RegularBanner, CelebrationBanner.
"""

import pygame

# Define global constants

#THIS IS WHAT GETS THE GUI UP:
pygame.init()

screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Soccer Game")

font = pygame.font.Font(None, 36)

#Define start button
startButton = pygame.Rect(150, 300, 200, 80)

#Define end button
endButton = pygame.Rect(450, 300, 200, 80)

#Keep list of buttons
buttList = [startButton, endButton]

isRunning = True

while isRunning:
    #Check every new event only one time
    for event in pygame.event.get():

        #User must click X to exit program
        if event.type == pygame.QUIT:
            isRunning = False

        #Detect one left mouse click
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:

                if startButton.collidepoint(event.pos):
                    print("Start button clicked")

                elif endButton.collidepoint(event.pos):
                    print("End button clicked")
                    isRunning = False

    #Draw the background of the game/field
    screen.fill("#57A839")

    #Draw start button
    pygame.draw.rect(screen, "black", startButton)
    startText = font.render("START", True, "white")
    startTextRect = startText.get_rect(center=startButton.center)
    screen.blit(startText, startTextRect)

    #Draw end button
    pygame.draw.rect(screen, "black", endButton)
    endText = font.render("END", True, "white")
    endTextRect = endText.get_rect(center=endButton.center)
    screen.blit(endText, endTextRect)

    #Put the completed drawing on the screen
    pygame.display.flip()

pygame.quit()


""" This base Banners class holds all banner types and forwards to the Banner that is actually called. """
class Banners:
    def __init__(self, font):
        # dictionary of banner names
        self.screens = {
            "Start": StartScreen(font),
            "Play": RegularBanner(font),
            "Celebration": CelebrationBanner(font),
            "End": EndScreen(font)
        }
        self.currentName = "Start"

    startButton = pygame.Rect(150, 300, 200, 80)
    endButton = pygame.Rect(450, 300, 200, 80)

    @property
    def current(self):
        return self.screens[self.currentName]

    def show(self, name):
        if name not in self.screens:
            raise ValueError(f"Unknown banner: {name}")

        self.currentName = name

    def handleEvent(self, event):
        return self.current.handleEvent(event)

    def update(self, dt):
        return self.current.update(dt)

    def draw(self, surface):
        self.current.draw(surface)


# StartScreen class:
# - start/exit buttons to start/end program
# - prompt user to pick team+rename team names; else keep default Team1+Team2 names
class StartScreen(Banners):
    def __init__(self, font, buttonType=None):
        self.font = font
        self.buttonType = buttonType


# EndScreen class:
# - stop all objects
# - display final score
# - option to restart match or end game (i.e. restart or end program)
class EndScreen(Banners):
    def __init__(self, font):
        self.font = font

    #pygame.draw.rect(screen, "black", restartButton)


# RegularBanner class:
# - contains scoreboard, timer, and team names
class RegularBanner(Banners):
    def __init__(self, font):
        self.font = font

    # TODO create scoreboard

    # TODO create timer

    # TODO box containing team names


# CelebrationBanner class:
# - displays when a team scores
# - resets player and Ball layout(i.e. configuration at the start of the game)
class CelebrationBanner(Banners):
    def __init__(self, font):
        self.font = font
