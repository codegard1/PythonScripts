# this version executes in a single stack frame
def factorial(x):
    i = x
    if x == 0:
        return 1
    else:
        while i > 1:
            i -= 1
            x *= i
        return x

print(factorial(100))

# This version makes a bigger stack, maybe?
# It depends on the compiler...
def factorial_recursive(i):
    if i == 0 or i == 1:
        return 1
    else:
        return i * factorial(i - 1)

print(factorial_recursive(100)) 
