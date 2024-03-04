#task Write a function that counts the number of vowels in a given word.
word = input("Provide a word: ")

def find_vowels(word):
    vowels_list = ["a","e","i","o","u","y"]
    vowels_sum = 0
    for letter in word:
        if letter in vowels_list:
            vowels_sum = vowels_sum +1        
    return vowels_sum 

print(find_vowels(word))
