import random

def guess(x):
    random_number = random.randint(1,x)
    user_found = 0
    print(random_number)
    while user_found != 1:
        user_guess = int(input("Enter your guess: "))
        if user_guess != random_number:
            if user_guess < random_number:
                print("Your guess is lower than the random number. Try something HIGHER")
            else:
                print("your guess is higher than the number. Try something LOWER")

        else:
            print(f"you have guessed the random number - {random_number}")
            user_found = 1
# guess(1000)


def computerGuess(my_imput):
    guessed = False
    low =1
    high =my_imput

    while guessed !=True:
        computer_random_guess = random.randint(low, high)
        if computer_random_guess == my_imput:
            print(f"Computer has guessed it right - {my_imput}")
            guessed = True
        else:
            print(f"I guessed {computer_random_guess}")
            hint= input("Is it high(h) or low(l)?")
            if hint == 'h':
                 high = computer_random_guess
            else:
                 low = computer_random_guess

computerGuess(200)
