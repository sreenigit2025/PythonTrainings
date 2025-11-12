
# a = 10
# b = 20

# if a > b:
#     print("a is greater than b 1")


# if a > b:
#     print("a is greater than b 2")
# else:
#     print("b is greater than a 2")    

# if a > b:
#     print("a is greater than b 3")
# elif b > a:
#     print("b is greater than a 3")
# else:
#     print("a and b are equal 3")

# a = 10
# b = 20
# c = 30

# if a > b and a > c:
#     print("a is the greatest 4")

# if a < b or a < c:
#     print("a is the greatest 5")

# i = 10
# str = " hello"

# print(f"type of i =  is {i}: {type(i)}")
# print(f"type of str =  is {str}: {type(str)}")

a = 10
b = 20

print("select the options:")
print("1. Add")
print("2. Subtract")
print("3. Multiplication")
print("4. Division")
option = int(input("Enter option (1 or 2 or 3 or 4): "))

if option == 1:
    print("You selected addition.")
    result = a + b
    print(f"The sum of a and b is: {result}")
elif option == 2:
    result = b - a
    print(f"The difference of b and a is: {result}")    
elif option == 3:
    result = a * b
    print(f"The product of a and b is: {result}")
elif option == 4:
    result = a / b
    print(f"The quotient of a and b is: {result}")
else:
    print("Invalid option selected.")


name =["sreeni", "kumar", "python"]

for n in name:
    if n.startswith("s"):
        print(f"{n} starts with s")
    else:
        print(f"{n} does not start with s")

for n in name:
    if n.startswith("s"):
        continue    
    print(f"{n} does not start with k")


for n in name:
    if n.startswith("s"):
        break   
    print(f"{n} does not start with k")