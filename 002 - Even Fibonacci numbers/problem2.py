def fib():
    a, b = 1, 2
    while True:
        yield a
        a, b = b, a + b

def main():

    sum = 0
    for val in fib():
        if val % 2 == 0 and val < 4000000:
            sum += val
        if val > 4000000:
            break
    print sum

main()