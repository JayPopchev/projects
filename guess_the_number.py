import random

def guess_the_number():
    computer_number = random.randrange(1, 100)
    guessed = False
    guesses_count = 0
    while not guessed:
        player_guess = int(input("Try to guess the number(1 - 100): "))
        guesses_count += 1
        if player_guess == computer_number:
            guessed = True
        elif player_guess > computer_number:
            print("Your guess is higher than the number!")
        else:
            print("Your guess is lower than the number!")
    print(f"Congratulations! You guessed the number - {computer_number} in {guesses_count} tries!")


def menu():
    print("Hello! Welcome to the guess the number game!")


def main_guess_the_number():
    menu()
    guess_the_number()