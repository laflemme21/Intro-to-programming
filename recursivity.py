def mult(x, y):
    if y == 1:
        return x
    else:
        return x+mult(x, y-1)


print(mult(4, 5))


def countdown(x):
    if x == 0:
        print(0)
    else:
        print(x)
        countdown(x-1)


countdown(5)


def list_cummulative_sum(x):
    if len(x) == 1:
        return [x[-1]]
    else:
        x[1] += x[0]
        return [x.pop(0)]+list_cummulative_sum(x)


print(list_cummulative_sum([1, 2, 3, 4, 5, 6, 7, 8, 9]))
