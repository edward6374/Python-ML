import sys
import time

def print_string(eta, percent, equals, elapsed, i, lst):
    string = "ETA: {}s [ {}%] [{}] {}/{} | elapsed time {}s".format(eta, percent, \
            ("=" * (equals - 1)) + (">" if equals > 0 else "") + \
            (" " * (50 - equals)), i, len(lst), elapsed) 
    print(string)

def ft_progress(lst):
    i = 0
    equals = 0
    percent = 0
    start_time = time.time()
    tick = (len(lst) / 50) / (len(lst) // 50)
    print("Tick:", tick, "Round:", (len(lst) // 50))
    print_string(0.0, percent, equals, 0.0, i, lst)
    while i < len(lst):
        i += 1
        percent = int((100 * i) / len(lst))
        equals = int(((100 * i) / len(lst)) / 2)
        elapsed = round(time.time() - start_time, 2)
        print_string(0.0, percent, equals, elapsed, i, lst)
        yield i

if __name__ == "__main__":
    ret = 0
    count = 0
    listy = range(3333)
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        time.sleep(0.005)
    print()
    print(ret)
