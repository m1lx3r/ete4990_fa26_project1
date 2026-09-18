# Author: Karim Yowkeem
# Course: ETE 4990 
# Purpose: Creates teams and different position groups


import json

from players import Goalkeeper, Striker, Midfielder, Defender1, Defender2

#Team class for the soccer game

class Team:
    # Create a team with a name and color
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.players = []

    #Add player to the team
    def add_player(self, player):
        if len(self.players) < 5:
            self.players.append(player)
            print(player.name, "was added to", self.name)
        else:
            print("The team already has five players.")

    #Display the team and all its players
    def show_team(self):
        print("\nTeam:", self.name)
        print("Color:", self.color)
        print("Players:")

        for player in self.players:
            print(
                player.number,
                "-",
                player.name,
                "-",
                player.position
            )

    #Find a player using their jersey number
    def find_player(self, number):
        for player in self.players:
            if player.number == number:
                return player

        return None

    #Draw every player on the team
    def draw_players(self, screen):
        for player in self.players:
            player.draw(
                screen,
                self.color,
                player.has_ball
            )

    #Find which player currently has the ball
    def get_player_with_ball(self):
        for player in self.players:
            if player.has_ball:
                return player

        return None

#Save both teams to the JSON file
def save_teams(team1, team2):
    game_data = []

    for team in [team1, team2]:
        team_data = {
            "name": team.name,
            "color": team.color,
            "players": []
        }

        for player in team.players:
            player_data = {
                "name": player.name,
                "number": player.number,
                "position": player.position,
                "class_name": player.__class__.__name__,
                "x": player.x,
                "y": player.y
            }

            team_data["players"].append(player_data)

        game_data.append(team_data)
    
    #the game data and what dump does in Python
    with open("teams.json", "w") as file:
        json.dump(game_data, file, indent=4)

    print("\nTeams saved successfully!")

#Load both teams from the JSON file, you can play with same teams so you dont have to write it again
def load_teams():
    try:
        with open("teams.json") as file:
            game_data = json.load(file)

    except FileNotFoundError:
        print("\nNo saved teams were found.")
        return None

    player_classes = {
        "Goalkeeper": Goalkeeper,
        "Striker": Striker,
        "Midfielder": Midfielder,
        "Defender1": Defender1,
        "Defender2": Defender2
    }

    loaded_teams = []

    for team_data in game_data:
        team = Team(team_data["name"], team_data["color"])

        for player_data in team_data["players"]:
            player_class = player_classes[player_data["class_name"]]

            player = player_class(
                player_data["name"],
                player_data["number"],
                player_data["x"],
                player_data["y"]
            )

            team.add_player(player)

        loaded_teams.append(team)

    print("\nTeams loaded successfully!")
    return loaded_teams[0], loaded_teams[1]
