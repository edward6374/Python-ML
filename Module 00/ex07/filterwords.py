import sys
import string

def filterwords():
    word = ""
    result = []
    letters = 0
    for i in sys.argv[1]:
        if i is not " " and i not in string.punctuation:
            letters += 1
            word += i
            print("Word:", word)
            print("Letters:", letters)
        elif (i is " " or i in string.punctuation):
            if letters > int(sys.argv[2]):
                result.append(word)
            word = ""
            letters = 0
    if letters > int(sys.argv[2]):
        result.append(word)
    print(result)

if __name__ == "__main__":
    print("ERROR") if len(sys.argv) != 3 or sys.argv[1].isdigit() or \
        not sys.argv[2].isdigit() else filterwords()
