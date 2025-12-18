
sentence = input("Enter a sentence: ")

# Number of characters (excluding nothing — count everything including spaces)
num_chars = len(sentence)
print("Number of characters:", num_chars)

# Number of words
words = sentence.split()
num_words = len(words)

print("Number of words:", num_words)

# Number of vowels
vowels = "aeiouAEIOU"
num_vowels = 0

for ch in sentence:
    if ch in vowels:
        num_vowels += 1
print("Number of vowels:", num_vowels)
