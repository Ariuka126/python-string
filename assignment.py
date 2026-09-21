# You can remove 'pass' if you written code in the function 

# Exercise 1
def count_characters(text):
    text=input("")
    num=len(text)
    return num

# Exercise 2
def remove_spaces(text):
    new_text=text.replace(" ","")
    return new_text

# Exercise 3
def count_vowels(text):
    count = 0
    for i in text:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            count += 1
    return count
# Exercise 4
def replace_vowels(text):
    new_text = text.replace("a","*")
    new_text = text.replace("i", "*")
    new_text = text.replace("e", "*")
    new_text = text.replace("o", "*")
    new_text = text.replace("u", "*")
    return new_text

# Exercise 5
def count_words(text):
    count=0
    text=text+" "
    for i in text:
        if i==" ":
            count+=1
    return count
# Exercise 6
def find_longest_word(text):
    sentence = input("  ")
    words = sentence.split()
    longest_word = max(words, key=len)
    return longest_word
