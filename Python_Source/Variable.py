# Global Variable declaration and static variable type checking
Name_team =20
Name1 = "sreeni"
Number1 = 10

# print statements
print(type(Name_team))
print(type(Name1))
print(type(Number1))

Name_team = input("Enter the team name :")
print("Team name is :" ,Name_team)

def f1():
    print("inside the function :" ,Name_team)

f1()

a = 1
if a == 1:
    b = 2