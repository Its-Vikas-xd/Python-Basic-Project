import random  # Importing the random module to generate random choices


# The computer randomly chooses between -1 (Water), 0 (Gun), and 1 (Snake)
computer = random.choice([-1, 0, 1])

# Taking input from the user
youstr = input("Enter Your Choice (s for Snake, w for Water, g for Gun): ")

# Dictionary to map user input to corresponding numerical values
youDict = {"s": 1, "w": -1, "g": 0}

# Dictionary to map numerical values back to their string representation
reverseDist = {1: "Snake", -1: "Water", 0: "Gun"}

# Converting user input to corresponding numerical value
you = youDict[youstr]

# Displaying choices of both user and computer
print(f" You Chose {reverseDist[you]} \n Computer Chose {reverseDist[computer]}")

# Checking for a draw condition
if computer == you:
    print("Match Draw")
else:
    # Checking win/lose conditions based on game rules

    # Snake (1) vs Water (-1) → Snake wins
    if computer == -1 and you == 1:
        print("You win!")

    # Water (-1) vs Gun (0) → Gun wins
    elif computer == -1 and you == 0:
        print("You lose!")

    # Snake (1) vs Water (-1) → Water loses
    elif computer == 1 and you == -1:
        print("You lose!")

    # Snake (1) vs Gun (0) → Gun wins
    elif computer == 1 and you == 0:
        print("You win!")

    # Gun (0) vs Water (-1) → Water loses
    elif computer == 0 and you == -1:
        print("You win!")

    # Gun (0) vs Snake (1) → Snake wins
    elif computer == 0 and you == 1:
        print("You lose!")

    # Error handling for unexpected input (shouldn't occur in normal conditions)
    else:
        print("Something wrong with this code ")  # Something is wrong
