import random

def play_game():
    """Play a game of rock-paper-scissors against the computer"""
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    user_choice = input("Enter 'rock', 'paper', or 'scissors': ")
    
    if user_choice not in options:
        print("Invalid choice! Try again.")
        return
    
    print(f"Computer chooses {computer_choice}")
    
    if user_choice == computer_choice:
        print("It's a tie!")
        return 0
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
        return 1
    else:
        print("Computer wins!")
        return -1