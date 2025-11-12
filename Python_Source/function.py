def firstfunc():
    print("This is first function")

firstfunc()

def add(a, b):
    sum = a + b
    return sum

result = add(10, 20)
print(f"The sum of 10 and 20 is: {result}")
print("***************")

# Type hinting in functions
def add(a:int, b):
    sum = a + b
    return sum

result = add(10, 20)
print(f"The sum of 10 and 20 is: {result}")
print("***************")

# return multiple values from function
def add():
    a =10
    b =20    
    return a,b

(x,y) = add()
print(f"a = {x} and b = {y}")

print("***************")

# default arguments in functions
def func1(a = 10, b = 20):
    sum = a + b
    return sum

result = func1()
print(f"The sum of default a and b is: {result}")
print("***************")

def age_validation(age:int = 18):
    if age < 0:
        return "Invalid age"
    elif age < 18:
        return "Minor"
    else:
        return "Adult"
    
result = age_validation(20)
print(f"Age validation result: {result}")

print("***************")    


