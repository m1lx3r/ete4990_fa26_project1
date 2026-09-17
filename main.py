# Author: Karim Yowkeem
# Course: ETE 4990 
# Purpose: Create or load two soccer teams and allow the user to choose which team to control


#Import player classes
from players import Goalkeeper, Striker, Midfielder, Defender1, Defender2

#Import Team class and JSON functions
from teams import Team, save_teams, load_teams


#Ask user to create one soccer team
def create_team(side):
    print("\nCreate your soccer team")

    team_name = input("Enter the team name: ")
    team_color = input("Enter the team color: ")

    team = Team(team_name, team_color)

    #Set starting positions based on the team's side
    if side == "left":
        positions = [
            ("Goalkeeper", Goalkeeper, 60, 250),
            ("Defender 1", Defender1, 170, 175),
            ("Defender 2", Defender2, 170, 325),
            ("Midfielder", Midfielder, 270, 250),
            ("Striker", Striker, 360, 250)
        ]

    else:
        positions = [
            ("Goalkeeper", Goalkeeper, 740, 250),
            ("Defender 1", Defender1, 630, 175),
            ("Defender 2", Defender2, 630, 325),
            ("Midfielder", Midfielder, 530, 250),
            ("Striker", Striker, 440, 250)
        ]

    #Create starting five players
    for position_name, player_class, x, y in positions:
        print("\nCreate your", position_name)

        player_name = input("Enter the player's name: ")

        #Keep asking if the number has already been used
        while True:
            try:
                player_number = int(input("Enter the player's number: "))

                if team.find_player(player_number) is None:
                    break

                print("Number has already been used. Pick a different number.")

            except ValueError:
                print("Please enter a whole number.")

        player = player_class(player_name, player_number, x, y)
        team.add_player(player)

    return team


#Display the front menu screen
print("\nSOCCER GAME")
print("1. Create new teams")
print("2. Load saved teams")

menu_choice = input("Choose option 1 or 2: ")

if menu_choice == "2":
    loaded_teams = load_teams()

    #If no files have been created, create new teams
    if loaded_teams is None:
        print("\nYou must create new teams.")

        print("\n--- TEAM 1 ---")
        team1 = create_team("left")

        print("\n--- TEAM 2 ---")
        team2 = create_team("right")

        save_teams(team1, team2)

    else:
        team1, team2 = loaded_teams

else:
    print("\n--- TEAM 1 ---")
    team1 = create_team("left")

    print("\n--- TEAM 2 ---")
    team2 = create_team("right")

    save_teams(team1, team2)

#Display both teams
team1.show_team()
team2.show_team()

#Ask which team the user wants to control
team_choice = input("\nChoose Team 1 or Team 2: ")

if team_choice == "1":
    user_team = team1

else:
    user_team = team2

print("\nYour team is", user_team.name)
print("You will control whichever teammate has the ball.")