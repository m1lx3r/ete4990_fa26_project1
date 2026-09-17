# Author: Karim Yowkeem
# Course: ETE 4990 
# Purpose: Create the different soccer player positions and control their movement and abilities

import pygame

#Classes for the soccer players

class Player:
    #Parent class for every soccer player

    def __init__(self, name, number, x, y):
        self.name = name
        self.number = number
        self.x = x
        self.y = y
        self.speed = 4
        self.position = "Player"
        self.has_ball = False

        #Moves the player while keeping them inside the field
    def move(self, change_x, change_y, field_width=800, field_height=500):
        self.x = self.x + change_x
        self.y = self.y + change_y

        #Stop the player at the left and right boundaries
        if self.x < 15:
            self.x = 15

        elif self.x > field_width - 15:
            self.x = field_width - 15

        #Stop the player at the top and bottom boundaries coordinates 800 and 500
        if self.y < 15:
            self.y = 15

        elif self.y > field_height - 15:
            self.y = field_height - 15

    #Draw player as a colored dot
    def draw(self, screen, color, controlled=False):
        try:
            player_color = pygame.Color(color)

        except ValueError:
            player_color = pygame.Color("blue")

        #Yellow circle shows which player is being controlled
        if controlled:
            pygame.draw.circle(
                screen,
                pygame.Color("yellow"),
                (self.x, self.y),
                19
            )

        pygame.draw.circle(
            screen,
            player_color,
            (self.x, self.y),
            15
        )

    def show_information(self):
        print("Name:", self.name)
        print("Number:", self.number)
        print("Position:", self.position)


class Goalkeeper(Player):
    #Goalkeeper controlled by the computer/AI

    def __init__(self, name, number, x, y):
        super().__init__(name, number, x, y)
        self.position = "Goalkeeper"
        self.goalkeeping = 10

    #Move the goalkeeper up or down toward the ball/verticle since the field is horizontal
    def move_ai(self, ball_y, field_height=500):
        if ball_y < self.y:
            self.y = self.y - self.speed

        elif ball_y > self.y:
            self.y = self.y + self.speed

        #Keep the goalkeeper inside the field/goal
        if self.y < 15:
            self.y = 15

        elif self.y > field_height - 15:
            self.y = field_height - 15


class Striker(Player):
    #Player with a high shooting skill

    def __init__(self, name, number, x, y):
        super().__init__(name, number, x, y)
        self.position = "Striker"
        self.shooting = 10


class Midfielder(Player):
    #Player with a high passing skill

    def __init__(self, name, number, x, y):
        super().__init__(name, number, x, y)
        self.position = "Midfielder"
        self.passing = 10


class Defender(Player):
    #Player with a high defense skill

    def __init__(self, name, number, x, y):
        super().__init__(name, number, x, y)
        self.position = "Defender"
        self.defense = 10


class Defender1(Defender):
    #First defender

    def __init__(self, name, number, x, y):
        super().__init__(name, number, x, y)


class Defender2(Defender):
    #Second defender

    def __init__(self, name, number, x, y):
        super().__init__(name, number, x, y)