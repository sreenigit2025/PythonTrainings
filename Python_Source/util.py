# age validation function with type hinting and default argument
def age_validation(age:int = 18) -> str:
    if age < 0:
        return "Invalid age"
    elif age < 18:
        return "Minor"
    else:
        return "Adult"
    

# default arguments in functions
def func1(a = 10, b = 20):
    sum = a + b
    return sum