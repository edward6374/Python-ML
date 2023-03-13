import sys
import string

def text_analyzer(arg):
    '''
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text
    '''

    spaces = 0
    punctuations = 0
    big_characters = 0
    small_characters = 0
    response = ""
    if arg == None or arg == "":
        response = input("Put something here: ")
    elif type(arg) != str:
        print("AssertionError: argument is not a string")
    else:
        response = arg
        for c in response:
            if c is " ":
                spaces += 1
            elif c in string.punctuation:
                punctuations += 1
            elif c.isupper():
                big_characters += 1
            elif c.islower():
                small_characters += 1
        print("The text contains", spaces + punctuations + big_characters + small_characters, "character(s):")
        print("-", big_characters, " upper letter(s)")
        print("-", small_characters, " lower letter(s)")
        print("-", punctuations, " punctuation mark(s)")
        print("-", spaces, " space(s)")

if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument are given")
    elif len(sys.argv) == 1:
        print("Give one argument to the program")
    else:
        text_analyzer(sys.argv[1])
