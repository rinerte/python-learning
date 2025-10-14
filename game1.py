import random

while True:
    print("Type 1- Scissors, 2- Rock, 3- Paper")
    user_input = input("Your choice: ")
    if user_input not in ['1', '2', '3']:
        print("Invalid input. Please try again.")
        continue
    user_choice = int(user_input)
    computer_choice = random.randint(1, 3)
    choices = {1: "Scissors", 2: "Rock", 3: "Paper"}
    print(f"You chose: {choices[user_choice]}")
    print(f"Computer chose: {choices[computer_choice]}")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        print("You win!")
    else:
        print("Computer wins!")

        