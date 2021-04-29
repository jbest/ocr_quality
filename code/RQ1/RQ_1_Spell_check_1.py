# Spell Checker using TextBlob and SpellChecker

from textblob import TextBlob
from spellchecker import SpellChecker
from textblob import Word
import re

# please refer to the RQ1 combined file where all txt files were combined and saved as combined.csv
file1 = "combined.csv"
with open(file1, "r+") as f:
    filecontent = f.read()
    print("Original Text:\n", str(filecontent))
    content = TextBlob(filecontent)
    fixed_words = ("Corrected text:\n", str(content.correct()))
    print(fixed_words)

# remove all punctuations before finding possible misspelled words
content_w_noPunc = re.sub(r'[^\w\s]', '', filecontent)
print("Printing Text without punctuations:\n", content_w_noPunc)
wordlist = content_w_noPunc.split(' ')
spell = SpellChecker(language='en')

# find those words that may be misspelled
misspelled = list(spell.unknown(wordlist))


print("***********Confidence level for each word within the file******************")
for word in wordlist:
    confidence_Level = Word(word)
    print()
    print(confidence_Level.spellcheck())

print("Possible list of misspelled words in the original text:\n", misspelled)
print("\nThe count of misspelled words in the original text:", len(misspelled), "words\n")

"""
#Possible candidate for misspelled word and other options
for word in misspelled:
    print("\nMost likely the option for the misspelled:")
    print(spell.correction(word))
    print("The other possible option for the misspelled word may be:""\n",(spell.candidates(word)))
"""

# finally save the text file with the corrected value
with open('Spellcheck_1.csv', "w") as f1:
    f1.write(str(content.correct()))