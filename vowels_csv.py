# 6. Modify the function created in task 5, but now as input use a csv file with words in it (ie. inputs.csv)
# Expected result: the function should create a txt file with dictionary which contains the input word as key, 
# dictionary with vowels, and the number of the vowels as value. It should look like this: {'banana' : {'a': 3}}
import pandas as pd 
data_csv = pd.read_csv("C:/Users/magda/OneDrive/Pulpit/Zadania_python/data.csv", header=None)
#print(data_csv)
df = pd.DataFrame(data=data_csv)
#print(df)
words = df[0].tolist()
#print(words)

def check_vowels(words):
    word_vowels_map={}
    for word in words:
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
        word_vowels_map[word]=dict
    return word_vowels_map

results = check_vowels(words)
print(results)   
f = open("vowels_text_file.txt","w")
f.write(str(results))
f.close()

