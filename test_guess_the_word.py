# CIS256 33975 FALL 2025    
# EX 4
# ---

# The test file for guess_the_word.py
import random 
import guess_the_word as gw

def test_user_get_random_word():
    word = gw.user_get_random_word()
    assert word in gw.The_words_list

def test_user_play_correct_guess():
    word = "Ajax"
    revealed = ["_"] * len(word)
    guess = "A"
    for index, letter in enumerate(word):
        if letter == guess:
            revealed[index] = guess
    assert revealed[0] == "A"

def test_user_play_incorrect_guess():
    word = "Chelsea"
    revealed = ["_"] * len(word)
    guess = "Z"
    for index, letter in enumerate(word):
        if letter == guess:
            revealed[index] = guess

    assert revealed == ["_"] * len(word)

def test_user_random_word_selection():
    random.seed(0) 
    word_1 = gw.user_get_random_word()
    random.seed(1)
    word_2 = gw.user_get_random_word()
    assert word_1 in gw.The_words_list
    assert word_2 in gw.The_words_list
    assert word_1 != word_2 or word_1 == word_2 
    
