def square(x):
    def check(x):
        if type(x) is int or type(x) is float:
            return True
    
    if check(x):
        return x**2 # = x*x
    else:
        return "Incorrect type"

def plus_one(x):
    return x+1        

if __name__ == "__main__":
    print(square(4))    
    print(square('abc'))
