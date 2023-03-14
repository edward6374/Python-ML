import sys
import string

letters = {
    "A" : ".-",
    "B" : "-...",
    "C" : "-.-.",
    "D" : "-..",
    "E" : ".",
    "F" : "..-.",
    "G" : "--.",
    "H" : "....",
    "I" : "..",
    "J" : ".---",
    "K" : "-.-",
    "L" : ".-..",
    "M" : "--",
    "N" : "-.",
    "O" : "---",
    "P" : ".--.",
    "Q" : "--.-",
    "R" : ".-.",
    "S" : "...",
    "T" : "-",
    "U" : "..-",
    "V" : "...-",
    "W" : ".--",
    "X" : "-..-",
    "Y" : "-.--",
    "Z" : "--..",
    "0" : "-----",
    "1" : ".----",
    "2" : "..---",
    "3" : "...--",
    "4" : "....-",
    "5" : ".....",
    "6" : "-....",
    "7" : "--...",
    "8" : "---..",
    "9" : "----.",
    " " : "/"
}

if __name__ == "__main__":
    result = ""
    if len(sys.argv) == 1:
        pass
    for i in sys.argv[1:]:
        if any(p in i for p in string.punctuation):
            print("ERROR")
            exit()
        result += i + " "
    result = result[:-1]
    for i in result:
        if i is " ":
            print(letters[" "], end=" ")
        else:
            if i.islower():
                i = i.upper()
            print(letters[i], end=" ")
    print()
