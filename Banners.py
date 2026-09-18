""" Author: Moises Santander """
""" Course: ETE 4990 FA2026 """
""" Purpose: Calls classes for other banners: StartScreen, EndScreen, RegularBanner, CelebrationBanner. """
import pygame

#THIS IS WHAT GETS THE GUI UP:
pygame.init()
screen = pygame.display.set_mode((800, 500))
isRunning = True # bool for whether the program is running

while isRunning:
    for event in pygame.event.get():
        # user must click "X" to exit program
        if event.type == pygame.QUIT:
            isRunning = False
                
    screen.fill("green")
    font = pygame.font.Font(None, 36)

    # Define start button
    startButton = pygame.Rect(150, 300, 200, 80)
    pygame.draw.rect(screen, "black", startButton)
    startText = font.render("START", True, "white")
    startTextRect = startText.get_rect(center=startButton.center)
    screen.blit(startText, startTextRect)

    # Define end button
    endButton = pygame.Rect(450, 300, 200, 80)
    pygame.draw.rect(screen, "black", endButton)
    endText = font.render("END", True, "white")
    endTextRect = endText.get_rect(center=endButton.center)
    screen.blit(endText, endTextRect)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # Detect a click on start+end buttons
    if event.type == pygame.MOUSEBUTTONDOWN:
        if startButton.collidepoint(event.pos):
            print("Start button clicked")

        elif endButton.collidepoint(event.pos):
            print("End button clicked")

pygame.quit()

""" This base Banners class holds all banner types and forwards to the Banner that is actually called. """
class Banners:
    def __init__(self, font):
        # dictionary of screen options
        self.screens = {"start": StartScreen(font),
                        "play": RegularBanner(font),
                        "celebration": CelebrationBanner(font),
                        "end": EndScreen(font)}
        self.active_name = "start"

    startButton = pygame.Rect(150, 300, 200, 80)
    endButton = pygame.Rect(450, 300, 200, 80)
    
    # list of buttons
    buttList = [startButton, endButton]


# StartScreen class:
# - start/exit buttons to start/end program
# - prompt user to pick team+rename team names; else keep default Team1+Team2 names
class StartScreen(Banners):
    def __init__(self, font, buttonType):
        self.font = font

    pygame.draw.rect(screen, "black", startButton)
    pygame.draw.rect(screen, "black", endButton)

    # Detect a click
    if event.type == pygame.MOUSEBUTTONDOWN:
        if startButton.collidepoint(event.pos):
            print("Start button clicked")

# EndScreen class:
# - stop all objects
# - display final score
# - option to restart match or end game (i.e. restart  or end program)
class EndScreen(Banners):
    def __init__(self, font):
        self.font = font

    #pygame.draw.rect(screen, "black", restartButton)
    pygame.draw.rect(screen, "black", endButton)

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
