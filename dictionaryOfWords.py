"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()

"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""
word_definitions["Awesome"] = "The feeling of students when they are learning Python"
word_definitions["Bad"] = "The feeling of students when they are not learning Python. :("
word_definitions["Potato"] = "Boil 'em, mash 'em, stick 'em in a stew."
word_definitions["Hobits"] = "Filthy stupid hobitses."


"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""

print(word_definitions["Potato"])
print(word_definitions["Hobits"])


"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""

for word in word_definitions:
    print("The definition of " + word + " is " + word_definitions[word])