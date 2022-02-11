<<<<<<< HEAD
from wordle import unique, hint_repeated_char as hrc, positions, check_guess, valid_guess_length
=======
from wordle import unique, hint_repeated_char, positions, check_guess
>>>>>>> 12558073ed8fd7238344bea70474f480f326e839

def test_hint_repeated_char() :
    assert hint_repeated_char([0,1], [0,1], ['_', '_']) == ['*', '*']

def test_hrc_letter_overlap() :
    assert hint_repeated_char([0,2], [1,2], ['_', '_', '_']) == ['$', '_', '*']

def test_hrc_letter_no_overlap():
    assert hint_repeated_char([0,1], [2], ['_','_','_']) == ['$','_','_']

def test_hrc_letter_no_overlap2():
    assert hint_repeated_char([0,2], [1], ['_','_','_']) == ['$','_','_']

def test_hrc_3():
    assert hint_repeated_char([0,1,2,3], [0,2,3], ['_','_','_','_']) == ['*','_','*','*']

def test_unique_oneletter() :
    assert unique('a', 0) == True

def test_unique_samelettertwice() :
    assert unique('aa', 0) == False

def test_unique_b_aba() :
    assert unique('aba', 1) == True

def test_unique_a_aba() :
    assert unique('aba', 2) == False

def test_unique_c_abcdee() :
    assert unique('abcdee', 2) == True

def test_unique_e_abcdee() :
    assert unique('abcdee', 5) == False

def test_positions_test_t() :
    assert positions('test', 't') == [0,3]
def test_positions_notfound() :
    positions('test', 'f') == []
def test_positions_test_e() :
    assert positions('test', 'e') == [1]
def test_positions_pizza_z() :
    assert positions('pizza', 'z') == [2,3]
def test_positions_zebra_z() :
    assert positions('zebra', 'z') == [0]

def test_check_guess_pizza_piano() :
    assert check_guess('pizza', 'piano') == '* * _ _ $'
def test_check_guess_pizza_zebra() :
    assert check_guess('pizza', 'zebra') == '_ _ $ _ *'
def test_check_guess_radio_bliss() :
    assert check_guess('radio', 'bliss') == '_ _ _ $ _'
def test_check_guess_radio_chefs() :
    assert check_guess('radio', 'chefs') == '_ _ _ _ _'
def test_check_guess_radio_radio() :
    assert check_guess('radio', 'radio') == '* * * * *'
def test_check_guess_icack_check() :
    assert check_guess('icack', 'check') == '_ $ _ * *'
def test_check_guess_ccbcc_cacbc() :
    assert check_guess('ccbcc', 'cacbc') == '* $ $ _ *'

<<<<<<< HEAD
def test_check_guess_length():
    assert valid_guess_length('pizza') == True



=======
#TODO write at least one test for `valid_guess_length`
#TODO write at least one test for `guess_in_dict`
#TODO write at least one test for `pick_word`
>>>>>>> 12558073ed8fd7238344bea70474f480f326e839
