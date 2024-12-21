import random


guess = int(input("Please, guess the number: "))

random_num = random.randint(1, 100)
trys = 0
while trys <= 10:
    if random_num == guess:
        print("wow, You guessed it right!") 
        trys += 1 
        replay = input("Do you want to play again? (yes/no): ")
        if replay in ["yes", 'yeah', 'y', 'Yes', 'YES']:
            random_num = random.randint(1, 100)
            guess = int(input("Please, guess the number: "))
            trys = 0
        if replay in ["no", 'No', 'NO', 'n', 'N']:
            print("Thank you for playing!")
            break
    elif abs(random_num - guess) < 5:
        print("You were so close!")
        trys += 1
        guess = int(input("Please, guess the number: "))
    elif abs(random_num - guess) < 10:
        print("You were close!")
        trys += 1
        guess = int(input("Please, guess the number: "))
    elif abs(random_num - guess) < 30:
        print("You were far!")
        trys += 1
        guess = int(input("Please, guess the number: "))
    elif abs(random_num - guess) < 50:
        print("You were very far!")
        trys += 1
        guess = int(input("Please, guess the number: "))
    elif abs(random_num - guess) < 100:
        print("You were extremely far!")
        trys += 1
        guess = int(input("Please, guess the number: "))
    else:
        print(f"You lost! The number was {random_num}")
        replay = input("Do you want to play again? (yes/no): ")
        if replay in ["yes", 'yeah', 'y', 'Yes', 'YES']:
            guess = int(input("Please, guess the number: "))
            trys = 0
        if replay in ["no", 'No', 'NO']:
            print("Thank you for playing!")
            break

   