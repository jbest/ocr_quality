# Using other other spellchecking methods

import language_check

# Mention the language keyword
tool = language_check.LanguageTool('en-US')
i = 0

# please refer to the RQ1 combined file where all txt files were combined and saved as combined.csv
with open(r'combined.csv', 'r') as fin:
    for line in fin:
        matches = tool.check(line)
        for mistake in matches:
            print(mistake)
        i = i + len(matches)
        pass

with open(r'combined.csv', 'rt') as file:
    for line in file:
        data = file.read()
        words = data.split()

print("Number of words in text file---->", len(words))
# prints total mistakes which are found
print("Total number of mistakes found in document is-----> ", i)
print("\nThe error ratio in the file is", len(words) / i)
print("***************************************\n")
