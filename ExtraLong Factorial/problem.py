def factorial(n):
    res = 1
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1

def extraLongFactorials(n):
    print(factorial(n))


if __name__ == '__main__':
    n = int(input())

    print(factorial(n))

