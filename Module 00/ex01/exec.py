import sys

if __name__ == "__main__":
    result = ""
    for i in sys.argv[1:]:
        result = result + i
    for i in result[-1::-1]:
        if i.isupper():
            i = i.lower()
        else:
            i = i.upper()
        print(i, end="")
    print()
