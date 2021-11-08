def square(x):
    def check(x):
        if type(x) is int or type(x) is float:
            return True
    
    if check(x):
        return x**2 # = x*x
    else:
        return "Incorrect type"
print(square(4))    
print(square('abc'))
