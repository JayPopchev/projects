import random

def win_lose_draw(player:str, computer:str)-> str: #expecting a string as a return
    if player == computer:
        print("It's a tie!")
        return "Draw"

    elif (player == "rock" and computer == "scissors") or \
            (player== "paper" and computer == "rock") or \
            (player == "scissors" and computer == "paper"):
        print(f"You win! +1 point! Computers choice - {computer}")
        return "Win"

    else:
        print(f"You lose! +1 for the computer! Computers choice - {computer}")
        return "Lose"

def game_rock_paper_scissors(num_of_games:int):
    choices = ["rock", "paper", "scissors"] #Three possible choices
    computer_score = 0
    player_score = 0
    for game in range(num_of_games):
        player_choice = input("Choose Rock, Paper or Scissors: ").lower()
        computer_choice = random.choice(choices)
        if player_choice not in choices:
            while not player_choice in choices:
                player_choice = input("Try again:\nChoose Rock, Paper or Scissors: ").lower()
        outcome = win_lose_draw(player_choice, computer_choice)

        if outcome == "Win":
            player_score += 1
        elif outcome == "Lose":
            computer_score += 1

    if player_score > computer_score:
        print(f"You win! Score {player_score}:{computer_score}")

    elif computer_score > player_score:
        print(f"You lose :( Score {player_score}:{computer_score}")

    else:
        print(f"Draw! Score {player_score}:{computer_score}")

def menu_rock_paper_scissors():
    print("Hello! Welcome to Rock-Paper-Scissors")
    number_of_games = int(input("How many games do you want to play? "))
    return number_of_games
def main_rock_paper_scissors():
    games = menu_rock_paper_scissors() #get the number of games
    game_rock_paper_scissors(games) #starting the game

