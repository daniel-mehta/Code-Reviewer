def factorial(n):
    # calculates factorial
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def greet(name):
    print("hello " + name)

greet("daniel")
print(factorial(5))
