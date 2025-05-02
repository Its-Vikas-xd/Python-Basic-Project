import random

# Generate a random number between 1 and 100
n = random.randint(1, 100)
a = -1
guessess = 0  # Corrected the variable name to "guesses" (optional)

while a != n:
    a = int(input("Guess the number: "))
    guessess += 1  # Move increment outside of conditions to count every guess
    
    if a > n:
        print("Lower Number Please")
    elif a < n:
        print("Higher Number Please")

# Display result
print(f"You have guessed the number {n} correctly in {guessess} attempts")
