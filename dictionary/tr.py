from PyDictionary import PyDictionary as pd
import sys
# n = sys.argv
# n=n[1:]
word = input('Enter the word/s with space separated : ')

word = word.split(' ')
dictionary = pd()
if len(word)>=1:
    for i in range(len(word)):
        print(word)
        try:
            meaning = dictionary.meaning(word[i])
            if meaning!=None:
                print(word[i] ,' : ' ,meaning)
                print()
                if i!=len(word)-1:
                    print('###########################################')
                    print()
            else:
                print('No meaning found in dictionary')
        except:
            print('No meaning found in dictionary')
else:
    print('No Word found')
