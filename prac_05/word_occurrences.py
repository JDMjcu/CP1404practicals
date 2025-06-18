""" 
Expected time: 20  Minutes 
Actual time: 18 Minutes for first ver, 30 minutes after fixing naming and sorting the list
JDM CP1404 
Word counter
"""


text = input("Text: ")

# Use .lower for the case of "A bee can be a queen and I can be a human" 
# prevents A from being classed as its own word.
words = text.lower().split(" ") 

word_to_count = {}

for word in words:
    frequency = words.count(word)
    word_to_count[word] = frequency

unique_words = sorted(list(word_to_count.keys()))

maximum_length = max(len(word) for word in unique_words)

for word in unique_words:
    print(f"{word:{maximum_length}} : {word_to_count[word]}")
