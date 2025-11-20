try:
    x = 10 / 0
except Exception as e:  # Catching all exceptions
    print("Error Type:", type(e).__name__)
    print("Error Message:", str(e))


# Handling multiple exceptions in Python using try-except block and else
try:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    result = x / y
except ValueError as e:
    print("Please enter only numbers!", str(e))
except ZeroDivisionError as e:
    print("Cannot divide by zero!", str(e))
else:
    print("Division result:", result)

print("**************************************")


# Handling multiple exceptions in Python using try-except block and else with finally

try:
    a = int(input("Enter number A: "))
    b = int(input("Enter number B: "))
    result = a / b
except ValueError:
    print("Please enter only numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("Result =", result)
finally:
    print("Program finished (finally block).")

print("**************************************")
