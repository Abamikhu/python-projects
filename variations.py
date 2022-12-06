#!/usr/bin/env python3.7

# Python implementation here
words = input("Enter a words: ")

str_lower = words.lower()
print("Lowercase:", str_lower)
# print ("Lowercase:", words.lower())

str_upper = words.upper()
print("Uppercase:", str_upper)

str_title = words.capitalize()
print("Capitalized:", str_title)

str_capitalize = words.title()
print("Title Case:", str_capitalize)

str_split = words.split()
print("Words:", str_split)

#sorted_words = sorted(words)
sorted_words = sorted(words)
#print(sorted_words)
#print("Alphabetic First Word:", sorted_words[0])
#print("Alphabetic Last Word:", sorted_words[-1])
first = str_split[0]
last = str_split[-1]
print("Fisrt word: " + first + ". ", "Last word: " + last + ".")

