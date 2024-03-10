#3. Write a function to check duplicate letters in words. It must accept strings ie. a sentence.
#The function should return True if any of the words has duplicate letters else return False.
#string = input("Provide your sentence to check duplicate letters: ")
def check_duplicates(sentence):
    words = sentence.split()
    for word in words:
        has_duplicates = find_duplicates_in_word(word)
        if has_duplicates:
            return True    
    return False

def find_duplicates_in_word(word):
    dict = {}
    for letter in word:
        if letter in dict:
            return True
        else:
            dict[letter] = 1
    return False 
