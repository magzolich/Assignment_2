#2. Write a word counter: as input program accepts a txt file, then reads the content from the file and as output prints the number of words in that txt file.

def word_counter(string):
    words = string.split()
    return len(words)


text_file = open("C:/Users/magda/OneDrive/Pulpit/Zadania_python/task2_text.txt",'r')
text_content = text_file.read()
words_count = word_counter(text_content)
print(words_count)