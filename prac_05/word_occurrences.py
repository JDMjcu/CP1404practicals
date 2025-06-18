""" 
Expected time: 20  Minutes 
Actual time: 18 Minutes
JDM CP1404 
Word counter
"""


sentence = input("Text: ")

words = sentence.split(" ")

print(words)

word_to_count = {}


# Count the number of times word is in list of words
# add that to the dictionary
for word in words:
    frequency = words.count(word)
    word_to_count[word] = frequency
    
print (word_to_count)

# to print nicely 
# get max length of charater use list comprehension and max function
# occording to criteria need to sort so most frequent are higher in the print

unique_words = list(word_to_count.keys())

maximum_length = max(len(word) for word in unique_words)

for word in unique_words:
    print(f"{word:{maximum_length}} : {word_to_count[word]}")


