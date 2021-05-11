print('Welcome to Hangman!')

game_word = input('Player 1 choose a word: ')
print('\n' * 100)
wrong_guess = []
right_guess = len(game_word) * ['']
lives = int(input('Player 1 choose the number of lives: '))
wrong_attempts = 0
out_of_lives = False
print(right_guess)


def find_index(guess_letter):
    for i, letter in enumerate(game_word):
        if letter == guess_letter:
            right_guess[i] = guess_letter


def stats(a, b, c, d):
    print('Correct guesses', a)
    print('Incorrect guesses', b)
    print('Lives remaining: ', c - d)


while not out_of_lives:
    if wrong_attempts < lives:
        guess = input('Guess a letter: ')
        if guess in game_word:
            find_index(guess)
            stats(right_guess, wrong_guess, lives, wrong_attempts)
            if all(letter in right_guess for letter in game_word):
                print('You win!')
                break
        else:
            if guess not in wrong_guess:
                wrong_guess.append(guess)
                wrong_attempts += 1
                stats(right_guess, wrong_guess, lives, wrong_attempts)
            elif guess in wrong_guess:
                print('You\'ve already tried that!')
    elif wrong_attempts == lives:
        out_of_lives = True
        print('You lose!')
        print('The word was', game_word)
