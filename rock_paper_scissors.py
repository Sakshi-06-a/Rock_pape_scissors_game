import random

def get_computer_choice():
    """Randomly select rock, paper, or scissors for computer"""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user, computer):
    """Decide who wins based on game rules"""
    if user == computer:
        return "tie"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "win"
    else:
        return "lose"

def play_game():
    print("="*40)
    print("Welcome to Rock-Paper-Scissors Game!")
    print("="*40)
    
    user_score = 0
    computer_score = 0
    
    while True:
        # 1. User Input
        user_choice = input("\nChoose: rock, paper, or scissors: ").lower()
        
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue
        
        # 2. Computer Selection
        computer_choice = get_computer_choice()
        
        # 3. Display Choices
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        # 4. Game Logic + Display Result
        result = determine_winner(user_choice, computer_choice)
        
        if result == "win":
            print("You Win! 🎉")
            user_score += 1
        elif result == "lose":
            print("You Lose! 😢")
            computer_score += 1
        else:
            print("It's a Tie! 🤝")
        
        # 5. Score Tracking
        print(f"\nScore - You: {user_score} | Computer: {computer_score}")
        
        # 6. Play Again
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("\nThanks for playing! Final Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            print("Goodbye! 👋")
            break

# Run the game
if __name__ == "__main__":
    play_game()
