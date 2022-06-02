# importing random module
import random

while True:
    R = "rock"
    P = "paper"
    S = "scissors"
    # collects user input
    Player = input("Make a choice (R, P or S): ")

    #DELETE THIS: Replacing user_action for Player AND CPU for computer_actionR
    options = ["R", "P", "S"]
    # receives computer's input
    CPU = random.choice(options)

    print (f"\nPlayer({Player}): CPU ({CPU}).\n")

    if Player == CPU:
        print(f"Both Player and CPU selected {Player}. It is a tie!")
    elif Player == "R":
        if CPU == "S":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose, CPU win!.")
    elif Player == "P":
        if CPU == "R":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cut paper! You lose, CPU win!")
    elif Player == "S":
        if CPU == "P":
            print("Scissor cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose, CPU win!")

    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != "y":
        break