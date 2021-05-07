def fib(num):
    if num == 1 or num == 2:
        return 1
    return fib(num-1) + fib(num-2)

def fib_series(num):
    start = 1
    while start <= num:
        print(fib(start))
        start+=1



if __name__ == '__main__':

    fib_series(7)

