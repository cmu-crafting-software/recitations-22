from lib2to3.pytree import LeafPattern
from tokenize import String
from typing import Final


# hint used for a character in the guess word that 
# does not appear in the answer_word
INCORRECT = "_"

# hint used for a character in the guess word that 
# appears in the answer word, but not in the same position
IN_WORD = "$"

# hint used for a character in the guess word that appears
# in the answer word in the same position
CORRECT = "*"

# string returned when guess is invalid
INVALID_GUESS = "Your guess is invalid."

# string returned when guess is invalid
<<<<<<< HEAD
SIZE : Final = 5
=======
SIZE = 5
>>>>>>> 12558073ed8fd7238344bea70474f480f326e839

# The number of days until an answer can be reused
DAYS_UNTIL_ANSWER_REUSED = 30

# returns true if ith letter in `word` is appears exactly once
# returns false otherwise
def unique(word, i) :
    letter_frequency = {}
    for j in range(len(word)) :
        k = word[j]
        if (letter_frequency.get(k)) :
            letter_frequency[k] = letter_frequency[k] + 1
        else :
            letter_frequency[k] = 1
    return letter_frequency[word[i]] == 1

# Input: a word and a character to look for
# Output: returns index list of occurrences `char` in `word`
def positions(word, char) :
    positions = []
    for i in range(len(word)) :
        if word[i] == char :
            positions.append(i)
    return positions

# Input:
# * `guess_positions` and `answer_positions` have equal length
# * list of integer indices to a char repeated in the answer
# * indices into guess or answer
# Output: 
# * returns modified copy of `hint``
def hint_repeated_char(guess_positions, answer_positions, hint) :
    matched = False
    hint_copy = hint[:]
    ap_copy = answer_positions[:]
    gp_copy = guess_positions[:]
    for pos in guess_positions :
        if pos in answer_positions :
            hint_copy[pos] = CORRECT
            ap_copy.remove(pos)
            gp_copy.remove(pos)
            matched = True
    if (matched) :
        return hint_repeated_char(gp_copy, ap_copy, hint_copy)
    else :
        num_in_word = len(answer_positions)
        count = 0
        for pos in guess_positions :
            if (count < num_in_word) :
                hint_copy[pos] = IN_WORD
                count = count + 1
        return hint_copy

# Input: two five character string
# Output: five character string where each character 
# is the INCORRECT, IN_WORD, or CORRECT character
# each character in the output corresponds to a character
# in the same position in the guess_word 
def check_guess(guess_word, answer_word) :
    # used to collect the hints for each character
    # in guess_word
    hint = ['_', '_', '_', '_', '_']
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
    for i in range(len(guess_word)) :
        if unique(guess_word, i) :
            if (guess_word[i]==answer_word[i]) :
                hint[i] = CORRECT
            elif (guess_word[i] in answer_word) :
                hint[i] = IN_WORD
        else : 
            hint = hint_repeated_char(
                positions(guess_word,guess_word[i]),
                positions(answer_word,guess_word[i]),
                hint
            )

    return ' '.join(hint)

def valid_guess_length(guess_word) :
    if len(guess_word) > SIZE :
    #TODO: check if `guess_word` is longer than SIZE
    #TODO: replace the line below
        return False
    else:
        return True

def guess_in_dict(guess_word, dict) :
    #TODO: check if `guess_word` is in the dictionary
    #TODO: replace the line below
    return False

# Input: the guess word, the answer word, and a dictionary of all possible guesses
#   assumes the answer word is in the dictionary
# Output: 
# If the guess is valid, output is the same as `check_guess`. If the guess is invalid,
# either because it is longer than SIZE or not in `dict` then the 
# output is the INVALID_GUESS string. 
def process_guess(guess_word, answer_word, dict) :
    if valid_guess_length(guess_word) :
        return INVALID_GUESS
    elif not(guess_in_dict(guess_word, dict)):
        return INVALID_GUESS
    return check_guess(guess_word, answer_word)

# Input: A dictionary where keys are valid wordle words and values are 
# are the last date the word was picked.
# Output: The answer word
# The dictionary will be modified such that the answer picked will have today's date as a value
def pick_word(dict) :
    #TODO: pick a random word from the dictionary
    #Hint: use the random python module. See: https://docs.python.org/3/library/random.html
    #TODO: stretch goal pick a random word that has not been used in DAYS_UNTIL_ANSWER_REUSED days
    
    #TODO: replace the line below
    return 'RADIO'