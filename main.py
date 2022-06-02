import random                                         # Let's import random procedure so that our CPU is unpredictable.

games_moves = ["R", "S", "P"]                         # Let's make a list of games moves we can chose from.
continue_playing = True                               # Let's keep this loop forever

while continue_playing == True:                       # This is to loop our program
    player_move = input("please what is your move: R: Rock, S: Scissors, P: Paper? ")          # This allows player to make move

    computer_move = random.choice(games_moves)          #This makes computer make moves randomly from the games_moves

    # Now let's know both the player's moves and computer's move.

    print("player chose", player_move, "computer_move", computer_move)

    # Now, we start defining the outcomes logically:

    if computer_move == player_move:
        print("This is a tie")

    elif player_move == "R":
        if computer_move == "P":
            print("Computer wins!")
            break
        elif computer_move == "S":
            print("Player wins!")
            break

    elif player_move == "S":
        if computer_move == "R":
            print("Computer wins!")
            break
        elif computer_move == "P":
            print("Player wins!")
            break

    elif player_move == "P":
        if computer_move == "S":
            print("Computer wins!")
            break
        elif computer_move == "R":
            print("Players wins!")
            break

    else:
        print("oops! Invalid move...Please try again by inputing the correct moves")
    

