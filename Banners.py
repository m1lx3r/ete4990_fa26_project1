# Author: Moises Santander
# Course: ETE 4990 FA2026
# Purpose: Calls classes for other banners: StartScreen, EndScreen, RegularBanner, CelebrationBanner.
import pygame

# define this base Banners class to open all banner types
class Banners:
    pygame.init()
    screen = pygame.display.set_mode((800, 500))
    isRunning = True # bool for whether the program is running

    while isRunning:
        for event in pygame.event.get():
            # user must click "X" to exit program
            if event.type == pygame.QUIT:
                isRunning = False

        screen.fill("green")

        startButton = pygame.Rect(150, 300, 200, 80)
        endButton = pygame.Rect(450, 300, 200, 80)

        # list of buttons
        buttList = [startButton, endButton]

        pygame.draw.rect(screen, "black", startButton)
        pygame.draw.rect(screen, "black", endButton)

        # flip() the display to put your work on screen
        pygame.display.flip()

    pygame.quit()


# StartScreen class:
# - start/exit buttons to start/end program
# - prompt user to pick team+rename team names; else keep default Team1+Team2 names

# EndScreen class:
# - stop all objects
# - display final score
# - option to restart match or end game (i.e. restart  or end program)

# RegularBanner class:
# - contains scoreboard, timer, and team names
# - is a parent of Scoreboard and Timer, which are displayed during play

# CelebrationBanner class:
# - displays when a team scores
# - resets player and Ball layout(i.e. configuration at the start of the game)
