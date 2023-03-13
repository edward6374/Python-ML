import sys

def calculus(a, b):
    print("Sum:\t\t", a + b)
    print("Difference:\t", a - b)
    print("Product:\t", a * b)
    if b == 0:
        print("Quotient:\t", "ERROR (division by zero)")
        print("Remainder:\t", "ERROR (modulo by zero)")
    else:
        print("Quotient:\t", a / b)
        print("Remainder:\t", a % b)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: python3 operations.py <number1> <number2>")
        print("Example:\n\tpython3 operations.py 10 3")
    elif len(sys.argv) > 3 or len(sys.argv) < 3:
        print("AssertionError: the program needs two arguments")
    elif not sys.argv[1].isnumeric() or not sys.argv[2].isnumeric():
        print("ValueError: one of the two arguments is not a number")
    else:
        calculus(int(sys.argv[1]), int(sys.argv[2]))
