import json
import string
import random

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
SIZE = 5

# The number of days until an answer can be reused
DAYS_UNTIL_ANSWER_REUSED = 30


class WordleGame:
    """
    `WordleGame` represents a Wordle game with both interactive and programmatic interfaces.
    """

    def __init__(self, dictionary_path, answer=None):
        """
        Constructs a `WordleGame` object with an optional `answer` word.
        """
        # load the dictionary
        self.words = load_words(dictionary_path)
        # if there's a predefined answer, use it
        if answer:
            self.answer_word = answer
        # otherwise, generate a new answer word from the dictionary
        else:
            self.answer_word = pick_word(self.words)
        # keep a history of guesses
        self.hint_history = []
        # keep a flag that indicates if the game has been won
        self.game_won = False
        # keep a __set__ of characters used in the game
        self.letters_used = set()
        # keep a __set__ of characters included in the answer
        self.used_answer_letters = set()

    def guess(self, guess_word):
        """
        Take a guess in the Wordle game. This function also records the guess if it's valid.
        """
        guess_result = process_guess(guess_word, self.answer_word, self.words)
        # update game state with new date if the guess is valid
        if guess_result != INVALID_GUESS:
            self.hint_history.append(guess_result)
            self.letters_used = self.letters_used.union(set(guess_word))
            self.used_answer_letters = self.used_answer_letters.union(
                filter(lambda c: c in self.answer_word, list(guess_word)))
            if guess_word == self.answer_word:
                self.game_won = True
        return guess_result

    def valid_letters(self):
        """
        Return a set of valid letters for the next guess, defined as:
        * Letters that are in the answer
        * OR letters that are not used so far

        NOTE: the wordle game keeps track of:
        * letters used by the player so far (`letters_used`)
        * letters used and in the answer so far (`used_answer_letters`)

        TODO: use these two pieces of info to compute the set of valid letters
        """
        # `alphabet` is a set of lowercase ASCII letters
        alphabet = set(string.ascii_lowercase)
        used_but_incorrect = self.letters_used.difference(self.used_answer_letters)
        return alphabet.difference(used_but_incorrect)

    def play(self, char_hint=False):
        """
        Play the wordle game in an interactive mode.
        """
        print("Welcome to Wordle. What is your first guess:")
        while(not self.game_won):
            guess = input()
            last_answer = self.guess(guess)
            print(display_hint(last_answer))
            if(char_hint):
                valid_chars = list(self.valid_letters())
                valid_chars.sort()
                print("Valid characters left: ", valid_chars)
            if self.game_won:
                print("YAY! You won! Tweet your result:")
                self.show_history()

    def show_history(self):
        """
        Print out the history of guesses in this game.
        """
        print("\n".join(map(lambda res: display_hint(res), self.hint_history)))


def unique(word, i):
    """
    returns true if ith letter in `word` is appears exactly once
    returns false otherwise
    """
    letter_frequency = {}
    for j in range(len(word)):
        k = word[j]
        if (letter_frequency.get(k)):
            letter_frequency[k] = letter_frequency[k] + 1
        else:
            letter_frequency[k] = 1
    return letter_frequency[word[i]] == 1


def positions(word, char):
    """
    Input: a word and a character to look for
    Output: returns index list of occurrences `char` in `word`
    """
    positions = []
    for i in range(len(word)):
        if word[i] == char:
            positions.append(i)
    return positions


def hint_repeated_char(guess_positions, answer_positions, hint):
    """
    Input:
    * `guess_positions` and `answer_positions` have equal length
    * list of integer indices to a char repeated in the answer
    * indices into guess or answer

    Output:
    * returns modified copy of `hint``
    """
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


def display_hint(hint):
    """
    Print out the hint.
    """
    if hint == INVALID_GUESS:
        return hint
    else:
        return ' '.join(hint)


def check_guess(guess_word, answer_word):
    """
    Input: two five character string
    Output: five character list where each character
    is the INCORRECT, IN_WORD, or CORRECT character
    each character in the output corresponds to a character
    in the same position in the guess_word
    """
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


def valid_guess_length(guess_word):
    """
    Output:
    * returns true if `guess_word` is SIZE characters long
    * returns false otherwise
    """
    return len(guess_word) == SIZE


def guess_in_dict(guess_word, dict):
    """
    Output:
    * returns true if `guess_word` is in `dict`
    * returns false otherwise
    """
    return guess_word in dict.keys()


def process_guess(guess_word, answer_word, dict):
    """
    Input: the guess word, the answer word, and a dictionary of all possible guesses
    assumes the answer word is in the dictionary
    Output:
    If the guess is valid, output is the same as `check_guess`. If the guess is invalid,
    either because it is longer than SIZE or not in `dict` then the
    output is the INVALID_GUESS string.
    """
    if not valid_guess_length(guess_word):
        return INVALID_GUESS
    elif not(guess_in_dict(guess_word, dict)):
        return INVALID_GUESS
    else:
        return check_guess(guess_word, answer_word)


def pick_word(words: dict):
    """
    Input: A dictionary where keys are valid wordle words and values are
    are the last date the word was picked.
    Output: The answer word, which has not been used in `DAYS_UNTIL_ANSWER_REUSED` days
    The dictionary will be modified such that the answer picked will have today's date as a value
    """
    random_word = ''
    while len(random_word) != 5:
        try:
            random_word = random.choice(list(words.keys()))
            assert len(random_word) == 5
        except AssertionError:
            pass
    return random_word


def load_words(path):
    """
    Load a dictionary from a file
    """
    with open(path) as json_file:
        words = json.load(json_file)
    return words


def play_wordle_games(n, dict_path):
    """
    Play the Wordle game `n` times.
    """
    
    for i in range(0,n,1):
        wordle = WordleGame(dict_path)
        wordle.guess(pick_word)
        wordle.guess(pick_word)
        wordle.guess(pick_word)
        wordle.guess(pick_word)
        wordle.guess(pick_word)
        wordle.show_history()
    # TODO: play the game n times:
    # TODO: instantiate a wordle game object
    # TODO: take 5 guesses randomly
    # TODO: print the history of guesses
    # TODO: report success rate
    


# if __name__ == "__main__":
#     dict_path = './words.json'
#     wordle = WordleGame(dict_path, answer = "apple")
#     wordle.guess("table")
#     wordle.guess("skate")
#     wordle.guess("apple")
#     wordle.show_history()
    #wordle.play(char_hint=True)
    # TODO: play the wordle game using methods in `WordleGame`
play_wordle_games(3, './words.json')