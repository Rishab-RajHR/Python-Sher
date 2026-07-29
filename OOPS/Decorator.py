# Decorators In Python

def decorate(func):
    def wrapper(a,b):
        print("The Addition to your numbers are ")
        func(a,b)
        print("Thank You I hope you liked it ")
    return wrapper

@decorate
def addition(a,b):
    print(f'Your total is {a + b}')

addition(12,87)