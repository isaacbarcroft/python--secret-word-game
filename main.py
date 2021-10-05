import random


wrong_guess=''
correct_guess=''
word_options=['gum', 'hurry', 'trigger', 'gunner', 'nature', 'python', 'wonderful', 'waterfall', 'dumpster', 'mansion', 'greatest', 'mountain']
word = random.choice(word_options)
def hangman(word):
    print()
    print('H A N G M A N')
    full_word = '_ ' * len(word)
    guesses = 7
    guessed = False
    words_guess=[]
    print('Guesses Left', guesses)
    print(full_word)
    print()
    while not guessed and guesses > 0:
        print()
        guess = input('Enter a letter    ')
        if guess.isalpha() and len(guess) == 1:
            if guess in words_guess:
                print('You already guessed', guess)
                print(words_guess)
                print()
                print(full_word)
            elif guess not in word:
                guesses = guesses - 1
                print(guess, 'is not in the word')
                words_guess.append(guess)
                print('Letters Guessed:', words_guess)
                print('Guesses Left', guesses)
                print(full_word)
            else: 
                print(guess, 'is in the word')
                words_guess.append(guess)
                word_list = list(full_word)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_list[index] = guess
                full_word = "".join(word_list)
                print(full_word)

            if full_word == word:
                print("You Win")
                guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in words_guess:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                guesses -= 1
                words_guess.append(guess)
            else:
                guessed = True
                full_word = word
        else: 
            print('TRY AGAIN')
    if guessed == True:
        print('You guessed the word!')

hangman(word)


#         if guess in word:
#             correct_guess = correct_guess + guess
#             print(guess, 'is in the word')
#         elif guess not in word:
#             print('Wrong guess')
#             guesses = guesses -1
#             wrong_guess = wrong_guess + guess
#             print('Wrong Guesses:', wrong_guess)
#             print('Correct Letters', correct_guess)
#     return False

# hangman(word, wrong_guess, correct_guess)

