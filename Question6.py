# Question : 6
import re
import string


def avg_len(s1):
    s = s1.translate(str.maketrans('','',string.punctuation)) # first I am removing all the punctuations, only spaces are left 
    words_count = 1 
    alphabets_count = 0
    for i in range(len(s)):
        if (s[i].isalpha()):
            alphabets_count+=1
        if s[i]==' ':          # check if there is space then it means a new word is starting so, I increment the word count by 1
            words_count +=1
    return alphabets_count/words_count
print(avg_len(",.one?:;"))
print(avg_len("Apple, orange, pear"))
