

def rek_fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return rek_fib(n-1) + rek_fib(n-2)

print(rek_fib(8))
