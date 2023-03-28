'''
1. ramon a word
loop starts run until
    lives are gone
    guesses correctly

if guessed right print yourbguessed right
else you failed

'''
import random

from words import words

def getRandomWord():
    randomword = random.choice(words)
    while '-' in randomword or ' ' in randomword:
        randomword = random.choice(words)
    return randomword


lives_left = 6
letters_used =[]
random_word = getRandomWord()
ifGuessed = False

print(random_word)
while lives_left != 0 and ifGuessed != True:

    word_list = []
    for x in random_word:
        if x in letters_used:
            word_list.append(x)
        else:
            word_list.append('-')
    print(f"\nyour word is; {word_list} and you have already guessed {letters_used}\n Lives Left {lives_left}")
    if '-' not in word_list:
        print("you won")
        ifGuessed = True
    else:
        user_guess = input("Guess a letter: ")

        if user_guess not in letters_used:
            letters_used.append(user_guess)
            if user_guess not in random_word:
                print(f"{user_guess} is not in word")
                lives_left = lives_left - 1
        elif user_guess in letters_used:
            print("you have guessed it ALREADY")

