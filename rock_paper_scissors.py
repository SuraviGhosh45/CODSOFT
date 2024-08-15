import random

def this_game():
    print("1. Rock\n2. Paper\n3. Scissors")
    try:
        user_choice = int(input("Enter Your Choice (1/2/3): "))
        if user_choice not in [1, 2, 3]:
            print("Invalid choice! Please select 1, 2, or 3.")
            return

        game = {1: "Rock", 2: "Paper", 3: "Scissors"}
        computer_choice = random.choice(list(game.keys()))

        print(f"Computer: {game[computer_choice]}")
        print(f"You: {game[user_choice]}")

        if computer_choice == user_choice:
            print("Draw!")
        else:
            if computer_choice == 1 and user_choice == 2:  # Rock vs Paper
                print("You Win!")
            elif computer_choice == 2 and user_choice == 1:  # Paper vs Rock
                print("You Lose!")
            elif computer_choice == 1 and user_choice == 3:  # Rock vs Scissors
                print("You Lose!")
            elif computer_choice == 3 and user_choice == 1:  # Scissors vs Rock
                print("You Win!")
            elif computer_choice == 2 and user_choice == 3:  # Paper vs Scissors
                print("You Win!")
            elif computer_choice == 3 and user_choice == 2:  # Scissors vs Paper
                print("You Lose!")
            else:
                print("Something went wrong")
    except ValueError:
        print("Invalid input! Please enter a number (1/2/3).")


this_game()

while True:
    ask = input("Want to Play again? Yes/No: ").strip().lower()
    if ask == "yes":
        this_game()
    elif ask == "no":
        feed = input("Give a Feedback here: ")
        print("Thank You!!")
        break
    else:
        print("Invalid input! Please type 'Yes' or 'No'.")
