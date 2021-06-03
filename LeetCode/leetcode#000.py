def func(a):
    if(a == 1):
        return 1
    return a * func(a - 1)

for x in range(1,10):
    print(func(x))


