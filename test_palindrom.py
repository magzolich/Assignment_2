#Task 1
#1. Write a program that as input accepts a string typed on keyboard and as output it will print this string reversed

import pytest

def palindrom_input():
    user_input = input("Please provide input text: ")    
    res = palindrom(user_input)
    print(res)

def palindrom(user_input):
    return user_input[::-1]
    
def test_palindrom():
    assert palindrom("kajak") == "kajak"
    assert palindrom("abc") == "cba"
    assert palindrom("35") == "53"
    assert palindrom("magda") == "adgam"
    with pytest.raises(TypeError):
        palindrom(15)


if __name__ == "__main__":
    palindrom_input()

