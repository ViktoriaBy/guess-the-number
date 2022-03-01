import random

num_random = random.randint(1, 100)

username = input("Howdy, what's your name?")
print(username, "I'm thinking of a number between 1 & 100.")


guessing = True
while guessing:
    guess = int(input("What is your guess?"))
    if guess > num_random:
        print("Too high!")
    elif guess < num_random:
        print("Too low!")
    else:
        print("Well, done", username)
        guessing = False
