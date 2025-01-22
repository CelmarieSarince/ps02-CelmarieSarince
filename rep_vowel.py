sentence = "Python is fun and Python is easy to learn!"
for letter in sentence:
    if letter.lower() in "aeiou":
        print(letter.upper(), end="")
    else:
        print(letter, end="")
