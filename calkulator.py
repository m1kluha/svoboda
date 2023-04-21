def fact(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res


actions = {'+': lambda x, y: x + y,
           '-': lambda x, y: x - y,
           '*': lambda x, y: x * y,
           '/': lambda x, y: x / y,
           '!': fact}

try:
    print("Введите два числа:")
    nums = map(int, input().split())
    print("Введите действие: +, -, *, /")
    operation = input()
    print(actions[operation](*nums))
except Exception as error:
    print(error)