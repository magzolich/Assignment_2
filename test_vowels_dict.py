from vowels_dict import check_vowels
def test():
    assert check_vowels("kot")=={"o":1}
    assert check_vowels("mleko")=={"e":1, "o":1}
    assert check_vowels("okno")=={"o":2}
    assert check_vowels("Aligator")=={'a': 2, 'i': 1, 'o': 1}