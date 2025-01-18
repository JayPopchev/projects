from projects.games.rock_paper_scissors import main_rock_paper_scissors
from projects.games.guess_the_number import main_guess_the_number
from projects.games.tic_tac_toe import main_tic_tac_toe

def menu():
    print("This are the available game:\n---1.Rock-Paper-Scissors\n---2.Guess the number\n---3.Tic-Tac-Toe\n---4.Connect 4")
    choice = input("Please select(1-4): ")
    return choice
def main():
    choice = menu()
    if choice == "1":
        main_rock_paper_scissors()

    if choice == "2":
        main_guess_the_number()

    if choice == "3":
        main_tic_tac_toe()

    if choice == "4":
        print("is still being made")
main()