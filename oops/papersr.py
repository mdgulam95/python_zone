import random
while True:
    possible_action =["rock","papers","scissor"]
    user_action=input("enter a choice[rock,paper,scissor]-> ")

    computer_action = random.choice(possible_action)
    print(f"\nyou chose {user_action},computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"both players selected {user_action}.its a tie")
    elif user_action == "rock":
        if computer_action == "scissor":
            print(f"rock smashes scissor.you win")
        else:
            print("paper covers rock.you lose")
    elif user_action == "paper":
        if computer_action == "rock":
            print("paper covers rock.you win")
        else:
            print("scissor cuts paper.you lose")
    elif user_action == "scissor":
        if computer_action == "paper":
            print("scissor cuts paper.you win")
        else:
            print("rock smashes scissor.you lose")
    
    play_again = input("play again?  (y/n):")
    if play_again.lower() != "y":
        
        print("Thank you for playing,bye")
        break

    