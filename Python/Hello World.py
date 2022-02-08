print("Hello world")
a = 1
b = 10
print(a+b)

def factorial(a):
    if (a<=1):
        return 1
    else:
        return factorial(a-1)*a

print(factorial(10))