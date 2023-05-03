"""Question 1 & 2: Prints each word in uppercase letter on a seperate line"""
def print_upper_words(words):
   for word in words:
     print(words.upper())

"""Question 3: Prints only words that start with letter 'e' or 'E' in uppercase"""
def print_upper_words(words):
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())

"""Question 4: Prints only words that start with letter 'e' or 'E' in uppercase"""
def print_upper_words(words, word_starts_with):
    for word in words:
        for letter in word_starts_with:
            if word.startswith(letter):
                print(word.upper())
                break