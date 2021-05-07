if __name__ == '__main__':
    def fib_calculator(num):
        if num == 1 or num == 2:
            return 1
        return fib_calculator(num-1) + fib_calculator(num-2)


    fib_dic = {1:1, 2:1}
    def fib(num):
        if num in fib_dic:
            print(fib_dic[num])
        else:
            fib_dic[num] = fib_calculator(num)
            print(fib_dic[num])