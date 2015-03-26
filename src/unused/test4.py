def c(num):
    if num % 2 == 0:
        res = 2*num
        if res > 10:
            return (num-1)
        return num%2
    return 2*num
