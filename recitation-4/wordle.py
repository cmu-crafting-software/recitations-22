import json
import random
from lib2to3.pytree import LeafPattern
from operator import truediv
from tokenize import Strin

# hint used for a character in the guess word that
# does not appear in the answer_word
INCORRECT = "🟥"

# hint used for a character in the guess word that
# appears in the answer word, but not in the same position
IN_WORD = "🟨"

# hint used for a character in the guess word that appears
# in the answer word in the same position
CORRECT = "🟩"

# string returned when guess is invalid
INVALID_GUESS = "Your guess is invalid."

# string returned when guess is invalid
SIZE = 5

# The number of days until an answer can be reused
DAYS_UNTIL_ANSWER_REUSED = 30


class WordleGame:
    '''
    `WordleGame` represents a Wordle game with both interactive and programmatic interfaces.
    '''

    def __init__(self, dictionary_path, answer=None):
        # load the dictionary
        self.words = load_words(dictionary_path)
        # if there's a predefined answer, use it
        if answer:
            self.answerWord = answer
        # otherwise, generate a new answer word from the dictionary
        else:
            self.answerWord = pick_word(self.words)
        # keep a history of guesses
        self.guess_history = []
        print("Answer is:", self.answerWord)

    def guess(self, guess_word):
        guess_result = process_guess(guess_word, self.answerWord, self.words)
        display_result = display_guess(guess_result)
        if not guess_result == INVALID_GUESS:
            self.guess_history.append(display_result)
        return display_result

    def play(self):
        print("welcome to Wordle, what is your first guess:")
        lastGuessCorrect = False
        while(not lastGuessCorrect):
            guess = input()
            lastGuessAnswer = self.guess(guess)
            print(lastGuessAnswer)
            if guess == self.answerWord:
                print("YAY! You won!")
                print("Tweet your progress:")
                print("\n".join(self.guess_history))
                lastGuessCorrect = True


def unique(word, i):
    '''
    returns true if ith letter in `word` is appears exactly once
    returns false otherwise
    '''
    letter_frequency = {}
    for j in range(len(word)):
        k = word[j]
        if (letter_frequency.get(k)):
            letter_frequency[k] = letter_frequency[k] + 1
        else:
            letter_frequency[k] = 1
    return letter_frequency[word[i]] == 1


def positions(word, char):
    '''
    Input: a word and a character to look for
    Output: returns index list of occurrences `char` in `word`
    '''
    positions = []
    for i in range(len(word)):
        if word[i] == char:
            positions.append(i)
    return positions


def hint_repeated_char(guess_positions, answer_positions, hint):
    '''
    Input:
    * `guess_positions` and `answer_positions` have equal length
    * list of integer indices to a char repeated in the answer
    * indices into guess or answer

    Output:
    * returns modified copy of `hint``
    '''
    matched = False
    hint_copy = hint[:]
    ap_copy = answer_positions[:]
    gp_copy = guess_positions[:]
    for pos in guess_positions:
        if pos in answer_positions:
            hint_copy[pos] = CORRECT
            ap_copy.remove(pos)
            gp_copy.remove(pos)
            matched = True
    if (matched):
        return hint_repeated_char(gp_copy, ap_copy, hint_copy)
    else:
        num_in_word = len(answer_positions)
        count = 0
        for pos in guess_positions:
            if (count < num_in_word):
                hint_copy[pos] = IN_WORD
                count = count + 1
        return hint_copy


def display_guess(hint):
    return ' '.join(hint)


def check_guess(guess_word, answer_word):
    '''
    Input: two five character string
    Output: five character string where each character
    is the INCORRECT, IN_WORD, or CORRECT character
    each character in the output corresponds to a character
    in the same position in the guess_word
    '''
    # used to collect the hints for each character
    # in guess_word
    hint = [INCORRECT, INCORRECT, INCORRECT, INCORRECT, INCORRECT]
    # `range`, like many functions in python has optional
    # arguments. The code below is equivalent to

    # If a letter appears multiple times in the guess word,
    # apply CORRECT first, then apply IN_WORD if more
    # appearances in guess than in use INCORRECT for remaining
    # letters (after CORRECT and IN_WORD have been applied)

    # `range(0, len(guess_word), 1)`.
    # `len(guess_word)` should be 5 assuming a valid guess
    # was given
    # correct loop first, always okay for multiple letters
    for i in range(len(guess_word)):
        if unique(guess_word, i):
            if (guess_word[i] == answer_word[i]):
                hint[i] = CORRECT
            elif (guess_word[i] in answer_word):
                hint[i] = IN_WORD
        else:
            hint = hint_repeated_char(
                positions(guess_word, guess_word[i]),
                positions(answer_word, guess_word[i]),
                hint
            )

    return hint

# Output:
# * returns true if `guess_word` is SIZE characters long
# * returns false otherwise


def valid_guess_length(guess_word):
    return len(guess_word) == SIZE

# Output:
# * returns true if `guess_word` is in `dict`
# * returns false otherwise


def guess_in_dict(guess_word, dict):
    return guess_word in dict.keys()

# Input: the guess word, the answer word, and a dictionary of all possible guesses
#   assumes the answer word is in the dictionary
# Output:
# If the guess is valid, output is the same as `check_guess`. If the guess is invalid,
# either because it is longer than SIZE or not in `dict` then the
# output is the INVALID_GUESS string.


def process_guess(guess_word, answer_word, dict):
    if not valid_guess_length(guess_word):
        return INVALID_GUESS
    elif not(guess_in_dict(guess_word, dict)):
        return INVALID_GUESS
    else:
        return check_guess(guess_word, answer_word)


def pick_word(dict):
    """
    Input: A dictionary where keys are valid wordle words and values are
    are the last date the word was picked.
    Output: The answer word, which has not been used in `DAYS_UNTIL_ANSWER_REUSED` days
    The dictionary will be modified such that the answer picked will have today's date as a value
    """
    # TODO: pick a random word from the dictionary
    # Hint: use the random python module. See: https://docs.python.org/3/library/random.html
    # TODO: stretch goal pick a random word that has not been used in DAYS_UNTIL_ANSWER_REUSED days
    random_word = ''
    while(not len(random_word) == 5):
        try:
            random_word = random.choice(list(dict.keys()))
            assert (len(random_word == 5))
        except:
            print("wrong Length word")
    return random_word


def load_words(path):
    with open(path) as json_file:
        words = json.load(json_file)
    return words


if __name__ == "__main__":
    dict_path = './words.json'
    wordle = WordleGame(dict_path)
    # wordle = WordleGame(dict_path, answer="rupea")
    wordle.play()
