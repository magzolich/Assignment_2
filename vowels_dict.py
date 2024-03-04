#5. Rewrite the function from task 4 and now it should return a dictionary with the vowel as key and the number of the vowel in a word as value.
word = input("Provide your word: ")

def check_vowels(word):
    dict = {}
    lower_word = word.lower()
    for letter in lower_word:
        vowels_list = ["a","e","i","o","u","y"]
        if letter not in vowels_list:
            continue
        if letter in dict:
            dict[letter]=dict[letter]+1  
        else:
            dict[letter] = 1
    return dict

print(check_vowels(word))    