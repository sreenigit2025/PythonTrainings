# Global Variable declaration and static variable type checking
Name_team =20
Name1 = "sreeni"
Number1 = 10

# print statements
print(type(Name_team))
print(type(Name1))
print(type(Number1))

#Name_team = input("Enter the team name :")
#print("Team name is :" ,Name_team)

def f1():
    print("inside the function :" ,Name_team)

f1()

a = 1
if a == 1:
    b = 2

# List operations

fruits = ["apple", "banana", "cherry"]

fruits.append("orange")          # ['apple', 'banana', 'cherry', 'orange']
fruits.insert(1, "grape")        # ['apple', 'grape', 'banana', 'cherry', 'orange']
fruits.remove("banana")          # ['apple', 'grape', 'cherry', 'orange']
fruits.pop()                     # removes 'orange'
print(fruits.index("cherry"))    # 2
print(fruits.count("apple"))     # 1
fruits.reverse()                 # ['cherry', 'grape', 'apple']
fruits.sort()                    # ['apple', 'cherry', 'grape']
new_list = fruits.copy()         # shallow copy

print(new_list)

#fruits.clear()     

sorted_list = sorted(fruits)
print(sorted_list)


reversed_list = fruits[::-1]
print(reversed_list)

if "apple" in fruits:
    print("Yes, apple is in the list!")