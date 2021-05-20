# Garbage Detecting using nostril

from nostril import nonsense
from nltk.tokenize import word_tokenize
from nltk.corpus import words

# please refer to the RQ1 combined file where all txt files were combined and saved as combined.csv
file1 = "combined.csv"

with open(file1, "r+") as file:
    text = file.read()
    words = word_tokenize(text)
    print(words)

# the minimum requirement to check the garbage word length is 6
for word in words:
    if (len(word)<7):
        #print(word)
        continue
    try:
        if nonsense(word):
            print(word,"is a nonsense word")
        else:
            #print(word, "is a real word")
            pass
    except Exception as e:
        pass
        #print('Word too short:', len(word), e)

print('done')