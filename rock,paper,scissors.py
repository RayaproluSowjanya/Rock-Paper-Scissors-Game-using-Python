import random
user_choice = int(input("Enter 0 for rock, 1 for Paper, 2 for Scissors : "))
if user_choice >= 3 or user_choice < 0:
    print("You entered an invalid number. You lose")
else:
    print("User Chose : ",user_choice)
    computer_choice = random.randint(0,2)
    print("Compter Chose : ",computer_choice)
    if user_choice == 2 and computer_choice == 0:
        print("You Lose")
    elif user_choice == 0 and computer_choice == 2:
        print("You Win")
    elif user_choice > computer_choice:
        print("You Win")
    elif user_choice < computer_choice:
        print("You Lose")
    elif user_choice == computer_choice:
        print("Draw...")