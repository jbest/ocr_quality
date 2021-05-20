# Garbage Detecting using nltk.corpus

from nltk.tokenize import word_tokenize
from nltk.corpus import words

# please refer to the RQ1 combined file where all txt files were combined and saved as combined.csv
file1 = "combined.csv"

with open(file1, "r+") as file:
    text = file.read()
    word = word_tokenize(text)
print("The whole content of the file is listed as below:\n", word)

final = []
for x in word:
    if x in words.words():
        final.append(x)
print("\nPrinting words without the gibberish value that exhibits no pattern\n", final)

# Comparing the values in two list ( word and final) and printing the difference that shows gibbersh words only
print("\nThe gibberish words founds from the combined file:\n", set(word) - set(final))
print("\nThe gibberish words count from the combined file:\n", (len(set(word) - set(final))))
