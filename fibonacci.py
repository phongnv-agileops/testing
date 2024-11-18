
# fibonacci.py
def fib(limit=100):
    a, b = 0, 1
    while a <= limit:
        yield a, a ** 2
        a, b = b, a + b

for f in fib():
    if f == 100:
        break
    print(f)
