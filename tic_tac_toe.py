def tic_tac_toe():
    grid = [[" " for _ in range(3)] for _ in range(3)]
    if_draw = False
    player_turn = "X"
    while True:
        for row_index in range(len(grid)):
            print(*grid[row_index], sep=" | ")

        row, col = [int(el) for el in input(f"Player {player_turn}, enter row and column (0-2): ").split()]

        if grid[row][col] == " ":
            grid[row][col] = player_turn

            for row in range(len(grid)):
                count = 0
                for coll in range(len(grid[row])):
                    if player_turn == grid[row][coll]:
                        count += 1
                    if count == 3:
                        print(f"Player {player_turn} wins")
                        exit()

            for coll in range(len(grid)):
                count = 0
                for row in range(len(grid)):
                    if player_turn == grid[row][coll]:
                        count += 1
                        if count == 3:
                            print(f"Player {player_turn} wins")
                            exit()
            count = 0
            for index in range(len(grid)):
                if player_turn == grid[index][index]:
                    count += 1
                if count == 3:
                    print(f"Player {player_turn} wins")
                    exit()

            count = 0
            for index in range(len(grid)):
                if player_turn == grid[index][len(grid) - 1 - index]:
                    count += 1
                if count == 3:
                    print(f"Player {player_turn} wins")
                    exit()
            if all(grid[row][col] != " " for row in range(3) for col in range(3)):
                print("It's a draw!")
                return

            if player_turn == "X":
                player_turn = "O"
            else:
                player_turn = "X"

        else:
            print("Taken, try again!")
def menu():
    print("Welcome to Tic-Tac-Toe")

def main_tic_tac_toe():
    menu()
    tic_tac_toe()