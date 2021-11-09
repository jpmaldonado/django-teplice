def my_decorator(func):
    def helper(val):
        print("Something will happen before")
        if func(val) is not None:
            print("Something will happen after")
        else:
            print("No values received")
        print('*'*50)

    return helper

@my_decorator
def greet(x):
    print(f"Ahoj! {x}")    

@my_decorator
def plus_one(x):
    return x+1

actions = [greet, plus_one]    

for action in actions:
    action(123)

def null_fun(x):
    print('abc')

print(my_decorator(null_fun(1)))