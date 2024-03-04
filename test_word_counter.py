from word_counter import word_counter

def test_word_counter():
    assert word_counter("Ala ma kota") == 3
    assert word_counter("Ladny dzisiaj mamy  dzien") == 4
    assert word_counter("Jaka jest twoja ulubiona ksiazka?") == 5
    