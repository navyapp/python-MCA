 #purpose - Generate Fibonacci series of N terms
def fibonacci(n):
    a, b = 0, 1
    while a < n:
        print(a)
        a, b = b, a + b
n = int(input("Enter the limit"))
fibonacci(n)