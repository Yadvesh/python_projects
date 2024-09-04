import random

# Input range and generate a random number
low = int(input("Enter the low range: "))
high = int(input("Enter the high range: "))
num = random.randint(low, high)

# Adjust num if it's equal to low or high
if num == low:
    num += 1
elif num == high:
    num -= 1

print(f"The chossen number will not be equal to {low} or {high}")

# Initial guess from the user
num_guess = int(input("Enter your guess: "))

if num_guess == num:
    print("You won! It took only 1 guess.")
else:
    counter = 1  # Start with 1 because the first guess has already been made
    while num_guess != num:
        counter += 1
        num_guess = int(input("Enter your guess: "))  # Convert input to integer
        print(f"This is your guess: {num_guess}")
        print(f"Number of guesses: {counter}")
    
    print(f"You won! It took you {counter} guesses.")
