# Author: Karim Yowkeem
# Course: ETE 4990 
# Purpose: Load and play the kicking, goal celebration, and background fan sounds


import pygame

#Sound class for the soccer game
class Sound:

    def __init__(self):
        self.kick_sound = None
        self.goal_sound = None
        self.fan_sound = None

    #Start the pygame sound system
    def start_mixer(self):
        if not pygame.mixer.get_init():
            pygame.mixer.init()

    #Load the kicking sound from a file
    def load_kick_sound(self, filename):
        self.start_mixer()
        self.kick_sound = pygame.mixer.Sound(filename)

    #Load the goal celebration sound from a file
    def load_goal_sound(self, filename):
        self.start_mixer()
        self.goal_sound = pygame.mixer.Sound(filename)

    #Load the background fans sound from a file
    def load_fan_sound(self, filename):
        self.start_mixer()
        self.fan_sound = pygame.mixer.Sound(filename)
        self.fan_sound.set_volume(0.3)

    #Play the kicking sound
    def play_kick_sound(self):
        if self.kick_sound is not None:
            self.kick_sound.play()

    #Play the goal celebration sound
    def play_goal_sound(self):
        if self.goal_sound is not None:
            self.goal_sound.play()

    #Play the fans sound continuously
    def play_fan_sound(self):
        if self.fan_sound is not None:
            self.fan_sound.play(loops=-1)

    #Stop the fans sound
    def stop_fan_sound(self):
        if self.fan_sound is not None:
            self.fan_sound.stop()