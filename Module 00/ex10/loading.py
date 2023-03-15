import sys
import time

def print_string(eta, percent, equals, elapsed, i, lst):
#    string = "ETA: {}{:.2f}s [{}%] [{}] {}/{} | elapsed time {}s".format("" if eta > 10.0 \
#            else " ", eta, str(percent) if percent == 100 else (" " + str(percent)) \
#            if percent > 9 else ("  " + str(percent)), \
#            ("=" * (equals - 1)) + (">" if equals > 0 else "") + \
#            (" " * (50 - equals)), i if i > 1000 else (" " + str(i)) \
#            if i > 100 else ("  " + str(i)), len(lst), round(elapsed, 2))
    string = "ETA: {}{:.2f}s [{}%] [{}] {}/{} | elapsed time {}s".format("" if eta > 10.0 \
            else " ", eta, str(percent) if percent == 100 else (" " + str(percent)) \
            if percent > 9 else ("  " + str(percent)), \
            ("\u25FC" * equals) + (" " * (50 - equals)), i if i > 1000 \
            else (" " + str(i)) if i > 100 else ("  " + str(i)), len(lst), round(elapsed, 2))
    print(string, end="\r")

def ft_progress(lst):
    i = 0
    eta = 0.0
    equals = 0
    percent = 0
    time_tick = 0.0
    start_time = time.time()
    tick = (len(lst) / 50) / (len(lst) // 50)
    print_string(eta, percent, equals, 0.0, i, lst)
    while i < len(lst):
        i += 1
        percent = int((100 * i) / len(lst))
        equals = int(((100 * i) / len(lst)) / 2)
        elapsed = time.time() - start_time
        if i == 2:
            time_tick = elapsed
            eta = time_tick * len(lst)
        else:
            eta = eta - time_tick
        print_string(eta, percent, equals, elapsed, i, lst)
        yield i
    eta = 0.0
    print_string(eta, percent, equals, elapsed, i, lst)

if __name__ == "__main__":
    ret = 0
    count = 0
    listy = range(3333)
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        time.sleep(0.005)
    print()
    print(ret)
