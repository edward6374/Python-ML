import sys

if __name__ == "__main__":
    number = 0;
    if len(sys.argv) == 1:
        print()
    elif len(sys.argv) > 2:
        print("AssertionError: more than one argument are provided")
    else:
        if not sys.argv[1].isnumeric():
            print("AssertionError: argument is not a number")
        else:
            for i in sys.argv[1]:
                number = number * 10 + int(i)
            if number == 0:
                print("I'm Zero.")
            elif number % 2 == 0:
                print("I'm Even.")
            else:
                print("I'm Odd.")
