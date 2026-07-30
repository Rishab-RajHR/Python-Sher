# Decorators In Python

def decorate(func):
    def wrapper(*args,**kwargs):
        print("The Addition to your numbers are ")
        func(*args,**kwargs)
        print("Thank You I hope you liked it ")
    return wrapper

@decorate
def addition(a,b):
    print(f'Your total is {a + b}')

addition(12,87)