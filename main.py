import random

game_letters = ["R", "P", "S"]
total_game_letters = ["R", "P", "S", "Q"]


def get_choice(guess):
    if guess == "Q":
        pass
    elif guess == "R":
        return "Rock"
    elif guess == "S":
        return "Scissors"
    elif guess == "P":
        return "Paper"
    else:
        return "Invalid input"
    

print('\n ******  Welcome to Rock-Paper-Scissors Game! :) ******')
print('[R] for Rock, [P] for Paper,[S] for Scissors and [Q] for Quit.')
print('You should pick an option from above. R, P and S to play and Q to Quit game. Always upper case ;)')


while True:
    
    # Possible choices from CPU and Player
    cpu_choice = random.choice(game_letters)
    player_choice = input("\nWrite your option here: ")

    # Checking valid inputs and possible quitting
    if player_choice not in total_game_letters:
        print('\nError: Invalid Input. You must select among R, P, S or Q. Always upper case.')
        print('Play again :)')
    elif player_choice == "Q":
        print('\nYou chose Q. Thanks for playing! See you next time!')
        break
    
    # Printing picked choice
    print("\n*** Player ({}) : CPU ({})".format(get_choice(player_choice), get_choice(cpu_choice)))

    # Checking players moves
    if player_choice == cpu_choice:
        print('Wow! It is a tie!. Play again :)')
        
    if player_choice == "R" and cpu_choice == "S":
        print('Congrats! Player is the winner, Rock beats Scissors. The program ends. Thanks for playing! :)')
        break
    elif player_choice == "P" and cpu_choice == "R":
        print('Congrats! Player is the winner, Paper beats Rock. The program ends. Thanks for playing! :)')
        break
    elif player_choice == "S" and cpu_choice == "P":
        print('Congrats! Player is the winner, Scissors beats Paper. The program ends. Thanks for playing! :)')
        break
    elif player_choice == "R" and cpu_choice == "P":
        print('CPU is the winner, Paper beats Rock. The program ends. Thanks for playing! :)')
        break
    elif player_choice == "P" and cpu_choice == "S":
        print('CPU is the winner, Scissors beats Paper. The program ends. Thanks for playing! :)')
        break
    elif player_choice == "S" and cpu_choice == "R":
        print('CPU is the winner, Rock beats Scissors. The program ends. Thanks for playing! :)')
        break
    