# Tic Tac Toe Game

# import required modules
import random
import sys

# a list of possible moves
moves = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

# a list to store the board
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

# display the board
def display_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# play again or main menu
def play_again():
    print("Would you like to:")
    print("1. Play Again")
    print("2. Main Menu")

    while True:
        choice = input("Please Enter your Choice: ")
        if choice == "1":
            play_game()
            break
        elif choice == "2":
            main_menu()
            break
        else:
            print("Invalid Input!")
            continue

# check for a winner
def check_winner():
    if board[0] == board[1] == board[2] != " ":
        return board[0]
    elif board[3] == board[4] == board[5] != " ":
        return board[3]
    elif board[6] == board[7] == board[8] != " ":
        return board[6]
    elif board[0] == board[3] == board[6] != " ":
        return board[0]
    elif board[1] == board[4] == board[7] != " ":
        return board[1]
    elif board[2] == board[5] == board[8] != " ":
        return board[2]
    elif board[0] == board[4] == board[8] != " ":
        return board[0]
    elif board[2] == board[4] == board[6] != " ":
        return board[2]
    elif " " not in board:
        return "tie"
    else:
        return None

# player turn
def player_turn():
    print("Player's turn")
    while True:
        choice = input("Please enter a move: ")
        if choice not in moves:
            print("Invalid Move! Try again")
            continue
        if board[int(choice)-1] != " ":
            print("This Space is Occupied! Try again")
            continue
        board[int(choice)-1] = "X"
        break

# computer turn
def computer_turn():
    print("Computer's turn")
    while True:
        choice = random.choice(moves)
        if board[int(choice)-1] != " ":
            continue
        board[int(choice)-1] = "O"
        break

# main game
def play_game():
    display_board()
    while True:
        player_turn()
        display_board()
        if check_winner() == "X":
            print("Player Wins!")
            break
        if check_winner() == "O":
            print("Computer Wins!")
            break
        if check_winner() == "tie":
            print("It's a tie!")
            break
        computer_turn()
        display_board()
        if check_winner() == "X":
            print("Player Wins!")
            break
        if check_winner() == "O":
            print("Computer Wins!")
            break
        if check_winner() == "tie":
            print("It's a tie!")
            break
    play_again()

# main menu
def main_menu():
    print("Welcome to Tic Tac Toe")
    print("1. Play Game")
    print("2. Quit")

    while True:
        choice = input("Please Enter your Choice: ")
        if choice == "1":
            play_game()
            break
        elif choice == "2":
            sys.exit()
        else:
            print("Invalid Input!")
            continue

# call the main menu
main_menu()
